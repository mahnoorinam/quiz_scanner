# Quiz Scanner & Grading System

## Description
A desktop application that automatically scans quiz answer sheets, detects filled bubbles, reads student information, and grades quizzes using computer vision.

## Features
- QR Code decoding to extract answer key
- OCR to read student name and registration number
- Bubble detection to identify selected answers
- Automatic grading with percentage and letter grade
- Batch processing of multiple quiz images
- Results exported to Excel file

## Installation

### Requirements
- Python 3.12+
- Tesseract OCR

### Install Tesseract
Download and install from:
https://github.com/UB-Mannheim/tesseract/wiki

### Install Python Libraries
pip install opencv-python pyzbar pillow pytesseract openpyxl pandas customtkinter

## How to Run
cd src
python main.py

## How to Use
1. Click "Upload Quiz Image"
2. Select a quiz answer sheet image
3. Click "Scan & Grade"
4. Results will be displayed on screen

## Batch Processing
To process multiple images and export to Excel:
cd src
python task5_batch.py
Results will be saved to output/results.xlsx

## Project Structure
quiz-scanner/
├── src/
│   ├── main.py          - Desktop App GUI
│   ├── task1_qr.py      - QR Code Decoding
│   ├── task2_ocr.py     - OCR Student Info
│   ├── task3_bubbles.py - Bubble Detection
│   ├── task4_grading.py - Grading Logic
│   └── task5_batch.py   - Batch Processing
├── samples/             - Quiz images
├── output/              - Excel results
└── demo/                - Screenshots

## Student
Name: Mahnoor, Alia
Course: Artificial Intelligence
Semester: SP2026
