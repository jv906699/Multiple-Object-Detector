import cv2
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from ultralytics import YOLO
import pandas as pd
from datetime import datetime
from collections import defaultdict
import os


class YOLOApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Multiple Object Detector")
        self.window.geometry("1100x850")

        # State
        self.model = None
        self.cap = None
        self.running = False

        # For recording detections
        self.recording = False
        self.results_data = []

        # For video recording
        self.video_recording = False
        self.video_writer = None
        self.video_save_path = None

        # Shared frame for smooth Tkinter update
        self.latest_frame = None
        self.frame_lock = threading.Lock()

        # --- UI Layout & Buttons ---
        title_label = tk.Label(window, text="Multiple Object Detector", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        self.video_label = tk.Label(window, bg="black")
        self.video_label.pack(padx=10, pady=10)

        button_frame = tk.Frame(window)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Load Model", command=self.load_model,
                  width=15, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Start", command=self.start_camera,
                  width=15, bg="#2196F3", fg="white").grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Stop", command=self.stop_camera,
                  width=15, bg="#f44336", fg="white").grid(row=0, column=2, padx=10)
        tk.Button(button_frame, text="Record Results", command=self.toggle_recording,
                  width=15, bg="#FF9800", fg="white").grid(row=0, column=3, padx=10)

        self.video_button = tk.Button(button_frame, text="Record Video", command=self.toggle_video_recording,
                                      width=15, bg="#9C27B0", fg="white")
        self.video_button.grid(row=0, column=4, padx=10)

        # Detection reading box
        self.detection_frame = tk.LabelFrame(window, text="Detected Objects (Live)", font=("Arial", 12, "bold"))
        self.detection_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.detection_text = tk.Text(self.detection_frame, height=10, font=("Consolas", 12))
        self.detection_text.pack(fill="both", expand=True, padx=10, pady=10)

        self.status_label = tk.Label(window, text="Status: Waiting for model...", font=("Arial", 12))
        self.status_label.pack(pady=10)

        # Start GUI update loop
        self.window.after(10, self.update_gui_frame)

    # ---------------------------------------------------
    # MODEL LOADING
    # ---------------------------------------------------
    def load_model(self):
        path = filedialog.askopenfilename(title="Select YOLO Weights", filetypes=[("PT Files", "*.pt")])
        if path:
            self.model = YOLO(path)
            self.status_label.config(text=f"Model Loaded: {os.path.basename(path)}")
            messagebox.showinfo("Success", "Model loaded successfully!")

    # ---------------------------------------------------
    # CAMERA START
    # ---------------------------------------------------
    def start_camera(self):
        if not self.model:
            messagebox.showwarning("Warning", "Please load a YOLO model first!")
            return

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Could not access camera.")
            return

        self.running = True
        self.status_label.config(text="Status: Camera started...")

        threading.Thread(target=self.process_frames, daemon=True).start()

    # ---------------------------------------------------
    # CAMERA STOP
    # ---------------------------------------------------
    def stop_camera(self):
        self.running = False
        self.status_label.config(text="Status: Camera stopped.")

        if self.video_recording:
            self.toggle_video_recording()

        if self.recording:
            self.toggle_recording()

        if self.cap:
            self.cap.release()
            self.cap = None

        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None

    # ---------------------------------------------------
    # FRAME PROCESSING THREAD (NO TKINTER HERE)
    # ---------------------------------------------------
    def process_frames(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue

            results = self.model(frame, verbose=False)
            annotated = results[0].plot()

            # For video recording
            if self.video_recording:
                if self.video_writer is None:
                    h, w = annotated.shape[:2]
                    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                    self.video_writer = cv2.VideoWriter(self.video_save_path, fourcc, 20.0, (w, h))
                self.video_writer.write(annotated)

            # Record detections
            if self.recording:
                for box in results[0].boxes.data.tolist():
                    x1, y1, x2, y2, conf, cls = box
                    self.results_data.append({
                        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "class": self.model.names[int(cls)],
                        "confidence": round(conf, 3)
                    })

            # Update detection text
            detected = defaultdict(list)
            for box in results[0].boxes.data.tolist():
                _, _, _, _, conf, cls = box
                detected[self.model.names[int(cls)]].append(conf)

            self.update_detection_box(detected)

            # Store frame for GUI
            with self.frame_lock:
                self.latest_frame = annotated.copy()

        # Cleanup
        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None

    # ---------------------------------------------------
    # UPDATE TEXT BOX (THREAD SAFE VIA after)
    # ---------------------------------------------------
    def update_detection_box(self, detected_objects):
        def update():
            self.detection_text.delete(1.0, tk.END)
            if detected_objects:
                for obj, conf_list in detected_objects.items():
                    avg_conf = sum(conf_list) / len(conf_list)
                    count = len(conf_list)
                    self.detection_text.insert(tk.END, f"{obj:15} × {count:<3} {avg_conf * 100:.2f}%\n")
            else:
                self.detection_text.insert(tk.END, "No objects detected...")

        self.window.after(1, update)

    # ---------------------------------------------------
    # GUI FRAME UPDATE LOOP (SMOOTH, NO FLICKER)
    # ---------------------------------------------------
    def update_gui_frame(self):
        if self.latest_frame is not None:
            with self.frame_lock:
                frame = cv2.cvtColor(self.latest_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(img)

            # Keep reference
            self.video_label.imgtk = imgtk
            self.video_label.config(image=imgtk)

        self.window.after(10, self.update_gui_frame)

    # ---------------------------------------------------
    # TOGGLE CSV RECORDING
    # ---------------------------------------------------
    def toggle_recording(self):
        if not self.recording:
            self.recording = True
            self.status_label.config(text="Recording detection results...")
        else:
            self.recording = False
            df = pd.DataFrame(self.results_data)
            df.to_csv("detections.csv", index=False)
            self.status_label.config(text="Saved detections.csv")
            messagebox.showinfo("Saved", "Predicted results saved to detections.csv")

    # ---------------------------------------------------
    # VIDEO RECORDING
    # ---------------------------------------------------
    def toggle_video_recording(self):
        if not self.video_recording:
            save = filedialog.asksaveasfilename(defaultextension=".mp4",
                                                filetypes=[("MP4 files", "*.mp4")])
            if not save:
                return
            self.video_save_path = save
            self.video_recording = True
            self.video_button.config(text="Stop Recording Video", bg="#E91E63")
            self.status_label.config(text="Recording video...")
        else:
            self.video_recording = False
            if self.video_writer:
                self.video_writer.release()
                self.video_writer = None
            self.video_button.config(text="Record Video", bg="#9C27B0")
            self.status_label.config(text="Video saved.")
            messagebox.showinfo("Saved", "Video saved successfully.")


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = YOLOApp(root)
    root.mainloop()
