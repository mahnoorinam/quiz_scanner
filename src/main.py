import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import os
import sys

sys.path.append(os.path.dirname(__file__))

from task1_qr import decode_answer_key
from task2_ocr import extract_student_info
from task3_bubbles import detect_bubbles
from task4_grading import grade_student

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class QuizScannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Scanner & Grading System")
        self.geometry("900x750")
        self.resizable(True, True)
        self.image_path = None
        self.build_ui()

    def build_ui(self):
        # Title
        title = ctk.CTkLabel(self, text="Quiz Scanner & Grading System",
                             font=ctk.CTkFont(size=22, weight="bold"))
        title.pack(pady=15)

        # Upload + Scan buttons
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=5)

        self.upload_btn = ctk.CTkButton(btn_frame, text="Upload Quiz Image / PDF",
                                        command=self.upload_image, width=200)
        self.upload_btn.pack(side="left", padx=10)

        self.process_btn = ctk.CTkButton(btn_frame, text="Scan & Grade",
                                         command=self.process_image,
                                         width=200, fg_color="green")
        self.process_btn.pack(side="left", padx=10)

        self.image_label = ctk.CTkLabel(self, text="No file selected",
                                        font=ctk.CTkFont(size=12))
        self.image_label.pack(pady=3)

        # Main content frame
        content_frame = ctk.CTkFrame(self)
        content_frame.pack(pady=5, padx=20, fill="both", expand=True)

        # Left — Student Info + Grade
        left_frame = ctk.CTkFrame(content_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(left_frame, text="Student Info & Grade",
                     font=ctk.CTkFont(size=15, weight="bold")).pack(pady=8)

        self.name_var    = ctk.StringVar(value="-")
        self.reg_var     = ctk.StringVar(value="-")
        self.set_var     = ctk.StringVar(value="-")
        self.score_var   = ctk.StringVar(value="-")
        self.percent_var = ctk.StringVar(value="-")
        self.grade_var   = ctk.StringVar(value="-")

        fields = [
            ("Student Name:",   self.name_var),
            ("Registration #:", self.reg_var),
            ("Set:",            self.set_var),
            ("Score:",          self.score_var),
            ("Percentage:",     self.percent_var),
            ("Grade:",          self.grade_var),
        ]

        for label_text, var in fields:
            row = ctk.CTkFrame(left_frame, fg_color="transparent")
            row.pack(fill="x", padx=10, pady=3)
            ctk.CTkLabel(row, text=label_text, width=130,
                         anchor="w").pack(side="left")
            ctk.CTkLabel(row, textvariable=var,
                         font=ctk.CTkFont(weight="bold")).pack(side="left")

        # Right — Answer Key + Student Answers
        right_frame = ctk.CTkFrame(content_frame)
        right_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(right_frame, text="Answer Key vs Student Answers",
                     font=ctk.CTkFont(size=15, weight="bold")).pack(pady=8)

        # Scrollable answer display
        self.answer_box = ctk.CTkTextbox(right_frame, width=350, height=400,
                                          font=ctk.CTkFont(size=13, family="Courier"))
        self.answer_box.pack(padx=10, pady=5, fill="both", expand=True)
        self.answer_box.insert("end", "Answers will appear here after scanning...")
        self.answer_box.configure(state="disabled")

        # Status
        self.status_label = ctk.CTkLabel(self, text="",
                                          font=ctk.CTkFont(size=12))
        self.status_label.pack(pady=8)

    def upload_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image and PDF Files", "*.jpg *.jpeg *.png *.pdf")]
        )
        if path:
            self.image_path = path
            self.image_label.configure(text=os.path.basename(path))
            self.status_label.configure(text="File loaded. Click Scan & Grade.")

    def process_image(self):
        if not self.image_path:
            messagebox.showwarning("Warning", "Please upload a file first.")
            return
        self.process_btn.configure(state="disabled")
        self.status_label.configure(text="Processing... please wait.")
        thread = threading.Thread(target=self.run_processing)
        thread.start()

    def run_processing(self):
        try:
            path = self.image_path
            if path.lower().endswith(".pdf"):
                import fitz
                doc = fitz.open(path)
                page = doc[0]
                pix = page.get_pixmap(dpi=200)
                path = path.replace(".pdf", "_converted.jpg")
                pix.save(path)

            answer_key     = decode_answer_key(path)
            if not answer_key:
                self.status_label.configure(text="ERROR: QR code not found.")
                self.process_btn.configure(state="normal")
                return

            student_info    = extract_student_info(path)
            student_answers = detect_bubbles(path)
            results         = grade_student(student_answers, answer_key)

            # Update student info
            self.name_var.set(student_info.get("name", "Not detected") or "Not detected")
            self.reg_var.set(student_info.get("reg", "Not detected") or "Not detected")
            self.set_var.set(answer_key.get("set", "-"))
            self.score_var.set(f"{results['total_score']} / {results['total_marks']}")
            self.percent_var.set(f"{results['percentage']:.1f}%")
            self.grade_var.set(results["grade"])

            # Build answer comparison text
            lines = []
            lines.append(f"{'Q':<6} {'Correct':<10} {'Student':<10} {'Result'}")
            lines.append("-" * 38)
            lines.append("--- Part-I ---")
            for q, correct in sorted(answer_key["part1"].items()):
                student = student_answers["part1"].get(q, "-")
                mark = "✓" if student == correct else "✗"
                lines.append(f"{q:<6} {correct:<10} {student:<10} {mark}")

            lines.append("")
            lines.append("--- Part-II ---")
            for q, correct in sorted(answer_key["part2"].items()):
                student = student_answers["part2"].get(q, "-")
                mark = "✓" if student == correct else "✗"
                lines.append(f"{q:<6} {correct:<10} {student:<10} {mark}")

            self.answer_box.configure(state="normal")
            self.answer_box.delete("1.0", "end")
            self.answer_box.insert("end", "\n".join(lines))
            self.answer_box.configure(state="disabled")

            self.status_label.configure(text="Done! Results displayed.")

        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}")
        finally:
            self.process_btn.configure(state="normal")


if __name__ == "__main__":
    app = QuizScannerApp()
    app.mainloop()