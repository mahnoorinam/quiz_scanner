import cv2
import fitz
import numpy as np

def detect_bubbles(image_path):
    """
    Detects filled bubbles in quiz answer sheet.
    Returns student answers for Part-I and Part-II.
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    bubbles = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 200 < area < 3000:
            x, y, w, h = cv2.boundingRect(cnt)
            aspect_ratio = w / float(h)
            if 0.7 < aspect_ratio < 1.3:
                bubbles.append((x, y, w, h))

    bubbles = sorted(bubbles, key=lambda b: (round(b[1] / 20) * 20, b[0]))

    answers = {"part1": {}, "part2": {}}
    options = ["A", "B", "C", "D"]

    part1_bubbles = [b for b in bubbles if b[0] < img.shape[1] // 2]
    part2_bubbles = [b for b in bubbles if b[0] >= img.shape[1] // 2]

    part1_rows = {}
    for b in part1_bubbles:
        row_key = round(b[1] / 20) * 20
        if row_key not in part1_rows:
            part1_rows[row_key] = []
        part1_rows[row_key].append(b)

    for i, (row_key, row_bubbles) in enumerate(sorted(part1_rows.items())):
        if i >= 8:
            break
        row_bubbles = sorted(row_bubbles, key=lambda b: b[0])
        filled_idx = get_filled_bubble(thresh, row_bubbles)
        if filled_idx is not None and filled_idx < 4:
            q_num = f"Q{i+1:02d}"
            answers["part1"][q_num] = options[filled_idx]

    part2_rows = {}
    for b in part2_bubbles:
        row_key = round(b[1] / 20) * 20
        if row_key not in part2_rows:
            part2_rows[row_key] = []
        part2_rows[row_key].append(b)

    for i, (row_key, row_bubbles) in enumerate(sorted(part2_rows.items())):
        if i >= 8:
            break
        row_bubbles = sorted(row_bubbles, key=lambda b: b[0])
        filled_idx = get_filled_bubble(thresh, row_bubbles)
        if filled_idx is not None and filled_idx < 4:
            q_num = f"Q{i+1:02d}"
            answers["part2"][q_num] = options[filled_idx]

    return answers


def get_filled_bubble(thresh, row_bubbles):
    """
    Checks which bubble in a row is filled.
    Returns index of filled bubble (0=A, 1=B, 2=C, 3=D).
    """
    max_fill = 0
    filled_idx = None

    for i, (x, y, w, h) in enumerate(row_bubbles):
        roi = thresh[y:y+h, x:x+w]
        fill_ratio = cv2.countNonZero(roi) / (w * h)
        if fill_ratio > max_fill:
            max_fill = fill_ratio
            filled_idx = i

    if max_fill > 0.4:
        return filled_idx
    return None


if __name__ == "__main__":
    image_path = "../samples/quiz sample.jpeg"
    answers = detect_bubbles(image_path)
    print("Detected Answers:")
    print(f"Part-I:  {answers['part1']}")
    print(f"Part-II: {answers['part2']}")