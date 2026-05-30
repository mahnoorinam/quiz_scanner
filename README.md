# 🎯 Quiz Scanner & Grading System

An intelligent desktop-based application that automatically scans quiz answer sheets, decodes QR-based answer keys, extracts student information, detects marked bubbles, grades quizzes, and generates structured reports.

Built as an **Artificial Intelligence (BSE-4A)** semester project for **SP2026**, this system combines **Computer Vision, OCR, QR Code Decoding, and Automated Grading** into one smart solution.

---

## 📌 Project Overview

Traditional quiz checking is time-consuming and prone to human error. This project automates the complete quiz evaluation process using image processing and AI-based techniques.

The system can:

✅ Decode QR-based answer keys  
✅ Read handwritten student details using OCR  
✅ Detect filled answer bubbles automatically  
✅ Grade quizzes instantly  
✅ Process multiple quiz sheets in batch mode  
✅ Export results to Excel reports

---

## ✨ Features

### 🔍 QR Code Decoding
- Detects QR codes from quiz sheets
- Extracts encoded answer keys
- Supports rotated or slightly skewed quiz images

### 📝 Student Information Extraction
- Reads **Student Name**
- Reads **Registration Number**
- Uses **OCR (Optical Character Recognition)**

### ⭕ Bubble Sheet Detection
- Detects marked bubbles (A/B/C/D)
- Handles:
  - ✔️ Filled answers
  - ➖ Unattempted questions
  - ⚠️ Multiple marked answers (invalid)

### 📊 Automatic Quiz Grading
- Compares student answers with answer key
- Calculates:
  - Correct answers
  - Incorrect answers
  - Unattempted questions
- Generates:
  - Percentage
  - Final marks
  - Letter Grade (A/B/C/D/F)

### 📁 Batch Processing
- Process multiple quiz sheets at once
- Automatically generates Excel reports
- Stores results in structured format

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.12+ | Core Development |
| OpenCV | Image Processing |
| Pyzbar | QR Code Detection |
| Tesseract OCR | Text Recognition |
| Pytesseract | OCR Integration |
| Pandas | Data Processing |
| OpenPyXL | Excel File Generation |
| Pillow | Image Handling |
| CustomTkinter | Desktop GUI |

---

## 📂 Project Structure

```bash
quiz_scanner/
│── src/
│   ├── main.py              # Main Desktop Application
│   ├── task1_qr.py          # QR Code Decoding
│   ├── task2_ocr.py         # Student Info Extraction
│   ├── task3_bubbles.py     # Bubble Detection
│   ├── task4_grading.py     # Quiz Grading Logic
│   └── task5_batch.py       # Batch Processing
│
├── samples/                 # Sample Quiz Images
├── output/                  # Generated Excel Reports
├── demo/                    # Screenshots / Demo Files
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mahnoorinam/quiz_scanner.git
cd quiz_scanner
```

---

### 2️⃣ Install Python Dependencies

Run the following command:

```bash
pip install opencv-python pyzbar pillow pytesseract openpyxl pandas customtkinter
```

---

### 3️⃣ Install Tesseract OCR

Download and install **Tesseract OCR** from:

🔗 https://github.com/UB-Mannheim/tesseract/wiki

After installation, make sure Tesseract is added to your system path.

---

## ▶️ Running the Application

Navigate to the source folder and run:

```bash
cd src
python main.py
```

---

## 🚀 How to Use

1. Launch the application  
2. Click **Upload Quiz Image**  
3. Select a quiz answer sheet image  
4. Click **Scan & Grade**  
5. View:
   - Student details
   - Detected answers
   - Score & grading report

---

## 📈 Batch Processing

To process multiple quiz sheets automatically:

```bash
cd src
python task5_batch.py
```

Generated reports will be saved in:

```bash
output/results.xlsx
```

---

## 📷 Demo & Screenshots

Add screenshots of:

- Desktop Interface  
- Quiz Upload Screen  
- Bubble Detection Result  
- Excel Report Output  

*(Recommended for better project presentation)*

---

## ✅ Tasks Completed

| Task | Description | Status |
|------|-------------|--------|
| Task 1 | QR Code Decoding | ✅ Completed |
| Task 2 | Student Info Extraction (OCR) | ✅ Completed |
| Task 3 | Bubble Sheet Reading | ✅ Completed |
| Task 4 | Quiz Grading | ✅ Completed |
| Task 5 | Batch Processing & Report Generation | ✅ Completed |

---

## 🎓 Academic Information

**Course:** Artificial Intelligence (BSE-4A)  
**Semester:** SP2026  


---

## 🔮 Future Improvements

- Real-time camera scanning  
- Better handwriting recognition  
- Mobile app version  
- AR-based live grading system  
- Improved accuracy for damaged quiz sheets

---

## 📜 License

This project was developed for **academic and educational purposes only**.

---

### ⭐ If you found this project helpful, consider giving it a star!
