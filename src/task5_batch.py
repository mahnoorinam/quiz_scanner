import os
import cv2
import pandas as pd
from task1_qr import decode_answer_key
from task2_ocr import extract_student_info
from task3_bubbles import detect_bubbles
from task4_grading import grade_student

def process_single_image(image_path, answer_key):
    """
    Processes a single quiz image and returns graded result.
    """
    print(f"\nProcessing: {image_path}")
    
    # Step 1: Get student info from OCR
    student_info = extract_student_info(image_path)
    
    # Step 2: Detect filled bubbles
    student_answers = detect_bubbles(image_path)
    
    # Step 3: Grade the student
    results = grade_student(student_answers, answer_key)
    
    return {
        "Name": student_info.get("name", "Unknown"),
        "Registration": student_info.get("reg", "Unknown"),
        "Set": answer_key.get("set", "Unknown"),
        "Part1_Score": results["part1_score"],
        "Part2_Score": results["part2_score"],
        "Total_Score": results["total_score"],
        "Total_Marks": results["total_marks"],
        "Percentage": round(results["percentage"], 1),
        "Grade": results["grade"]
    }


def process_batch(samples_folder, output_folder):
    """
    Processes all images in samples folder and saves results to Excel.
    """
    # Get all image files
    valid_extensions = ['.jpg', '.jpeg', '.png']
    image_files = [
        f for f in os.listdir(samples_folder)
        if os.path.splitext(f)[1].lower() in valid_extensions
    ]
    
    if not image_files:
        print("No images found in samples folder.")
        return
    
    print(f"Found {len(image_files)} image(s) to process.")
    
    all_results = []
    answer_key = None
    
    for image_file in image_files:
        image_path = os.path.join(samples_folder, image_file)
        
        # Get answer key from QR code of first image
        if answer_key is None:
            answer_key = decode_answer_key(image_path)
            if answer_key is None:
                print(f"Could not decode QR from {image_file}, skipping.")
                continue
        
        result = process_single_image(image_path, answer_key)
        result["Image"] = image_file
        all_results.append(result)
        print(f"Done: {image_file} -> Grade: {result['Grade']}, Score: {result['Total_Score']}/{result['Total_Marks']}")
    
    if not all_results:
        print("No results to save.")
        return
    
    # Save to Excel
    df = pd.DataFrame(all_results)
    
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, "results.xlsx")
    df.to_excel(output_path, index=False)
    
    print(f"\nResults saved to: {output_path}")
    print("\nSummary:")
    print(f"Total Students: {len(all_results)}")
    print(f"Average Score:  {df['Total_Score'].mean():.1f}/{all_results[0]['Total_Marks']}")
    print(f"Average Grade:  {df['Grade'].mode()[0]}")
    print("\nAll Results:")
    print(df[["Name", "Registration", "Total_Score", "Percentage", "Grade"]].to_string(index=False))


if __name__ == "__main__":
    samples_folder = "../samples"
    output_folder = "../output"
    process_batch(samples_folder, output_folder)