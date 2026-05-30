# 🎯 Quiz Scanner & Grading System

An intelligent desktop application that automatically scans quiz answer sheets, extracts student information, detects marked answers, grades quizzes, and generates structured reports using Computer Vision and OCR.

This project automates the traditional quiz checking process, making evaluation faster, more accurate, and efficient.

---

## ✨ Features

### 🔍 QR Code Decoding
- Detects and decodes QR codes from quiz sheets
- Extracts answer keys automatically
- Supports slightly rotated or skewed images

### 📝 Student Information Extraction
- Extracts **Student Name**
- Extracts **Registration Number**
- Uses **OCR (Optical Character Recognition)**

### ⭕ Bubble Sheet Detection
- Detects selected answers (A/B/C/D)
- Handles:
  - ✅ Filled answers
  - ➖ Unattempted questions
  - ⚠️ Multiple selected answers

### 📊 Automatic Quiz Grading
- Compares student answers with the answer key
- Calculates:
  - Correct answers
  - Incorrect answers
  - Unattempted questions
- Generates:
  - Final Score
  - Percentage
  - Letter Grade

### 📁 Batch Processing
- Processes multiple quiz sheets automatically
- Exports results to Excel
- Generates structured reports

---

## 🛠️ Libraries & Tools Used

| Library / Tool | Purpose |
|----------------|---------|
| Python | Core Programming Language |
| OpenCV | Image Processing & Bubble Detection |
| Pyzbar | QR Code Decoding |
| Tesseract OCR | Text Recognition |
| Pytesseract | OCR Integration |
| Pandas | Data Processing |
| OpenPyXL | Excel Report Generation |
| Pillow (PIL) | Image Handling |
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
├── demo/                    # Screenshots
│   ├── ss 1.png             # Main Interface
│   └── ss 2.png             # Output / Result Screen
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mahnoorinam/quiz_scanner.git
cd quiz_scanner
```

---

### 2️⃣ Install Required Libraries

Run the following command:

```bash
pip install opencv-python pyzbar pillow pytesseract openpyxl pandas customtkinter
```

---

### 3️⃣ Install Tesseract OCR

Download and install **Tesseract OCR**:

🔗 https://github.com/UB-Mannheim/tesseract/wiki

After installation, make sure Tesseract is properly configured in your system path.

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
3. Select a quiz sheet image  
4. Click **Scan & Grade**  
5. View:
   - Student Details
   - Detected Answers
   - Final Score & Grade

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

## 📷 Screenshots

### 🖥️ Main Interface

![Main Interface](demo/ss%201.png)

### 📊 Scan Result / Output

![Output Result](demo/ss%202.png)

---

## ✅ Completed Tasks

| Task | Description | Status |
|------|-------------|--------|
| Task 1 | QR Code Decoding | ✅ Completed |
| Task 2 | Student Information Extraction (OCR) | ✅ Completed |
| Task 3 | Bubble Sheet Reading | ✅ Completed |
| Task 4 | Quiz Grading | ✅ Completed |
| Task 5 | Batch Processing & Report Generation | ✅ Completed |

---

## 🔮 Future Improvements

- Real-time camera scanning
- Improved handwriting recognition
- Mobile application support
- AR-based live quiz grading
- Better image correction for low-quality scans

---

## 👩‍💻 Contributors

- Mahnoor Inam
- Alia  Ahmad

---

## 📜 License

This project is intended for **educational and academic purposes only**.

---

⭐ If you like this project, consider giving it a star!
