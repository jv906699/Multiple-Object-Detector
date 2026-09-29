<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,45:1e293b,75:2563eb,100:06b6d4&height=220&section=header&text=MULTIPLE%20OBJECT%20DETECTOR&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=34&desc=YOLOv12%20%E2%80%A2%20PYTORCH%20%E2%80%A2%20REAL-TIME%20COMPUTER%20VISION&descSize=17&descAlignY=57&descColor=ffffff"
    width="100%"
    alt="Multiple Object Detector"
  />
</p>

<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&pause=900&color=2563EB&center=true&vCenter=true&repeat=true&width=720&height=32&lines=Multi-Class+Object+Detection;YOLOv12+%7C+PyTorch;Real-Time+Inference;Dataset+%E2%86%92+Training+%E2%86%92+Evaluation+%E2%86%92+Detection"
    alt="Multiple Object Detector capabilities"
  />
</p>

<p align="center">
  <kbd>YOLOv12</kbd>
  &nbsp;&nbsp;
  <kbd>PYTORCH</kbd>
  &nbsp;&nbsp;
  <kbd>OBJECT DETECTION</kbd>
  &nbsp;&nbsp;
  <kbd>REAL-TIME AI</kbd>
</p>
# 🎯 Project Overview

**Multiple Object Detector** is a real-time multi-class object detection system built with **YOLOv12 and PyTorch**. The project covers the complete computer-vision workflow — from dataset preparation and model training to evaluation and real-time inference.

The system was developed to detect **10 object classes** using a custom dataset and provides trained model weights together with a GUI-based inference application for visualizing detections.

---

# 📌 Key Highlights

| Category | Details |
|---|---|
| 🤖 Detection Model | YOLOv12 |
| 🧠 Deep Learning Framework | PyTorch |
| 🎯 Detection Type | Multi-Class Object Detection |
| 🏷️ Object Classes | 10 |
| 🖼️ Dataset | 17,542 images |
| 🔥 Training | 50 epochs |
| 📈 mAP@0.5 | 93.8% |
| 📊 mAP@0.5:0.95 | 57.8% |
| ⚡ Inference | Real-Time Detection |
| 🖥️ Interface | GUI-Based Inference |
| 💾 Model Output | Trained YOLO Weights |

---

# 🔄 End-to-End Workflow

```text
DATASET
   ↓
DATASET PREPARATION
   ↓
YOLOv12 TRAINING
   ↓
MODEL EVALUATION
   ↓
TRAINED WEIGHTS
   ↓
REAL-TIME INFERENCE
   ↓
GUI VISUALIZATION

```
# 🔄 Detection Pipeline

<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&pause=800&color=2563EB&center=true&vCenter=true&repeat=true&width=780&height=36&lines=DATASET+%E2%86%92+DATASET+PREPARATION;DATASET+PREPARATION+%E2%86%92+YOLOv12+TRAINING;YOLOv12+TRAINING+%E2%86%92+MODEL+EVALUATION;MODEL+EVALUATION+%E2%86%92+TRAINED+WEIGHTS;TRAINED+WEIGHTS+%E2%86%92+REAL-TIME+INFERENCE;REAL-TIME+INFERENCE+%E2%86%92+GUI+VISUALIZATION"
    alt="Multiple Object Detector pipeline"
  />
</p>

<p align="center">
  <kbd>DATASET</kbd>
  →
  <kbd>PREPARATION</kbd>
  →
  <kbd>YOLOv12</kbd>
  →
  <kbd>EVALUATION</kbd>
  →
  <kbd>WEIGHTS</kbd>
  →
  <kbd>INFERENCE</kbd>
  →
  <kbd>GUI</kbd>
</p>

<p align="center">
  <sub>
    End-to-end workflow from dataset preparation to real-time object detection.
  </sub>
</p>

# 🧠 Dataset & Training

The detector was trained using a custom object-detection dataset prepared for multi-class YOLO training.

## 📦 Dataset Overview

| Dataset Property | Details |
|---|---|
| 🖼️ Total Images | 17,542 |
| 🏷️ Detection Classes | 10 |
| 🤖 Model Architecture | YOLOv12 |
| 🧠 Training Framework | PyTorch |
| 🔥 Training Duration | 50 epochs |
| 📦 Dataset Format | YOLO-compatible object detection dataset |

---

## 🔧 Training Workflow

<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&pause=850&color=2563EB&center=true&vCenter=true&repeat=true&width=760&height=36&lines=DATASET+COLLECTION+%E2%86%92+ANNOTATION;ANNOTATION+%E2%86%92+DATASET+PREPARATION;DATASET+PREPARATION+%E2%86%92+YOLOv12+TRAINING;YOLOv12+TRAINING+%E2%86%92+MODEL+EVALUATION;MODEL+EVALUATION+%E2%86%92+TRAINED+MODEL+WEIGHTS"
    alt="YOLOv12 training workflow"
  />
</p>

<p align="center">
  <kbd>DATASET</kbd>
  &nbsp;→&nbsp;
  <kbd>ANNOTATION</kbd>
  &nbsp;→&nbsp;
  <kbd>PREPARATION</kbd>
  &nbsp;→&nbsp;
  <kbd>TRAINING</kbd>
  &nbsp;→&nbsp;
  <kbd>EVALUATION</kbd>
  &nbsp;→&nbsp;
  <kbd>WEIGHTS</kbd>
</p>

---

## ⚙️ Training Configuration

| Parameter | Configuration |
|---|---|
| Model | YOLOv12 |
| Framework | PyTorch |
| Dataset Size | 17,542 images |
| Number of Classes | 10 |
| Training Epochs | 50 |
| Output | Trained model weights |

The trained weights are then used for inference and real-time visualization through the project's detection interface.

# 📊 Model Performance

The trained YOLOv12 detector was evaluated on the prepared object-detection dataset using standard object-detection metrics.

## 📈 Evaluation Results

| Metric | Result |
|---|---:|
| **mAP@0.5** | **93.8%** |
| **mAP@0.5:0.95** | **57.8%** |

### Understanding the Metrics

| Metric | Description |
|---|---|
| **mAP@0.5** | Mean Average Precision calculated at an IoU threshold of 0.50 |
| **mAP@0.5:0.95** | Mean Average Precision averaged across IoU thresholds from 0.50 to 0.95 |

The results provide two complementary views of the detector's performance: detection quality at a fixed IoU threshold and performance across a broader range of localization thresholds.

---

## 🎯 Performance Summary

<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&pause=900&color=2563EB&center=true&vCenter=true&repeat=true&width=680&height=36&lines=mAP%40.5+%E2%86%92+93.8%25;mAP%40.5%3A0.95+%E2%86%92+57.8%25;YOLOv12+%E2%86%92+10-Class+Object+Detection"
    alt="Model performance summary"
  />
</p>

# 🖥️ Real-Time Detection & GUI

The trained YOLOv12 weights can be used for real-time object detection through the project's inference application.

The detection interface provides a visual way to run the trained model and inspect its predictions on incoming frames.

## 🔍 Inference Workflow

<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&pause=850&color=2563EB&center=true&vCenter=true&repeat=true&width=760&height=36&lines=LOAD+TRAINED+WEIGHTS+%E2%86%92+INPUT+FRAME;INPUT+FRAME+%E2%86%92+YOLOv12+INFERENCE;YOLOv12+INFERENCE+%E2%86%92+OBJECT+DETECTIONS;OBJECT+DETECTIONS+%E2%86%92+BOUNDING+BOXES+%2B+LABELS;ANNOTATED+FRAME+%E2%86%92+REAL-TIME+GUI+DISPLAY"
    alt="Real-time detection workflow"
  />
</p>

<p align="center">
  <kbd>WEIGHTS</kbd>
  &nbsp;→&nbsp;
  <kbd>INPUT</kbd>
  &nbsp;→&nbsp;
  <kbd>INFERENCE</kbd>
  &nbsp;→&nbsp;
  <kbd>DETECTIONS</kbd>
  &nbsp;→&nbsp;
  <kbd>VISUALIZATION</kbd>
  &nbsp;→&nbsp;
  <kbd>GUI</kbd>
</p>

---

## 🎯 Detection Output

For each processed frame, the detector can provide visual information such as:

| Output | Purpose |
|---|---|
| Bounding Boxes | Localize detected objects |
| Class Labels | Identify detected object classes |
| Confidence Scores | Indicate model confidence |
| Annotated Frames | Visualize detection results |
| Multiple Detections | Detect multiple objects within the same frame |

---

## 🖥️ GUI-Based Inference

The project includes a GUI-based interface for running the trained detector and visualizing model predictions.

The interface provides a more accessible way to interact with the trained model without requiring the inference pipeline to be operated entirely from the command line.

### Inference Flow

```text
Trained YOLOv12 Weights
          ↓
     Input Source
          ↓
    YOLOv12 Inference
          ↓
   Object Predictions
          ↓
Bounding Boxes + Labels
          ↓
      GUI Display

```
# 📸 Detection Results

The trained YOLOv12 model was evaluated across a variety of images containing different object classes and multi-object scenes. The inference results demonstrate the model's ability to localize and classify multiple objects within the same image.

## 🎯 Multi-Class Detection

<p align="center">
  <img
    src="./results/val_batch0_pred%20(4).jpg"
    width="49%"
    alt="YOLOv12 multi-class detection results"
  />
  <img
    src="./results/val_batch1_pred%20(4).jpg"
    width="49%"
    alt="YOLOv12 multi-object detection results"
  />
</p>

The predictions include multiple classes such as **person, laptop, cell phone, cup, bottle, chair, book, remote, dining table, and handbag**, with bounding boxes and confidence scores displayed directly on the inference outputs.

---

## 📊 Confusion Matrix

<p align="center">
  <img
    src="./results/confusion_matrix_normalized%20(4).png"
    width="85%"
    alt="Normalized confusion matrix for YOLOv12 detector"
  />
</p>

The normalized confusion matrix provides a class-level view of the detector's predictions across the evaluated classes, showing the distribution of correct predictions and class-level confusion.

---

## 🔎 Detection Output

| Output | Description |
|---|---|
| Bounding Boxes | Localize detected objects within the image |
| Class Labels | Identify the predicted object class |
| Confidence Scores | Display the model's confidence for each detection |
| Multi-Object Detection | Detect multiple objects within the same image |
| Class-Level Evaluation | Analyze prediction behavior using the confusion matrix |

# 📁 Project Structure

The repository contains the trained YOLOv12 model, inference application, dataset configuration, evaluation results, and supporting project documentation.

```text
Multiple-Object-Detector/
│
├── 📂 results/
│   ├── 📊 confusion_matrix (4).png
│   ├── 📊 confusion_matrix_normalized (4).png
│   ├── 📈 BoxP_curve*.png
│   ├── 📈 BoxR_curve*.png
│   ├── 🖼️ train_batch*.jpg
│   ├── 🖼️ val_batch*_labels*.jpg
│   ├── 🖼️ val_batch*_pred*.jpg
│   └── 📄 results.csv
│
├── 🤖 best.pt
├── 🤖 last.pt
├── ⚙️ data.yaml
├── 🏷️ classes.txt
├── 🖥️ detector_gui.py
├── 🎥 new test 1.mp4
├── 📄 Project Introduction.pdf
│
└── 📖 README.md

```

# ⚙️ Installation & Usage

## 🧩 Requirements

The GUI application is built with Python and uses the following libraries:

| Package | Purpose |
|---|---|
| `ultralytics` | YOLO model loading and inference |
| `opencv-python` | Camera access and frame processing |
| `Pillow` | Image conversion and GUI image display |
| `pandas` | Recording detection results to CSV |
| `tkinter` | Graphical user interface |

Python standard-library modules such as `threading`, `datetime`, `collections`, and `os` are also used by the application.

---

## 📦 Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/jv906699/Multiple-Object-Detector.git
cd Multiple-Object-Detector

```
# 🛠️ Tech Stack

<p align="center">
  <kbd>PYTHON</kbd>
  &nbsp;&nbsp;
  <kbd>YOLOv12</kbd>
  &nbsp;&nbsp;
  <kbd>PYTORCH</kbd>
  &nbsp;&nbsp;
  <kbd>OPENCV</kbd>
  &nbsp;&nbsp;
  <kbd>TKINTER</kbd>
  &nbsp;&nbsp;
  <kbd>PILLOW</kbd>
  &nbsp;&nbsp;
  <kbd>PANDAS</kbd>
</p>

## 🧩 Technology Roles

| Technology | Role in the Project |
|---|---|
| **Python** | Core application and inference logic |
| **YOLOv12** | Object detection model |
| **PyTorch** | Deep-learning framework used by the YOLO pipeline |
| **OpenCV** | Camera access, frame capture, and video processing |
| **Tkinter** | GUI application interface |
| **Pillow** | Image conversion and GUI image rendering |
| **Pandas** | Detection-result data recording and CSV generation |

---

# 🚀 Project Capabilities

| Capability | Implementation |
|---|---|
| 🎯 Multi-Class Detection | Detect multiple object classes within the same frame |
| 📦 Custom Trained Model | Uses trained YOLO `.pt` weights |
| 📹 Real-Time Camera Input | Processes frames from the default camera |
| 🖼️ Detection Visualization | Displays annotated frames with bounding boxes |
| 📊 Live Detection Summary | Shows detected classes, counts, and average confidence |
| 💾 Result Recording | Saves detection records to CSV |
| 🎥 Video Recording | Saves annotated detection output as MP4 |
| 🖥️ Desktop GUI | Provides a graphical interface for operating the detector |
| 🔄 Model Selection | Allows users to load a YOLO `.pt` model through the GUI |
