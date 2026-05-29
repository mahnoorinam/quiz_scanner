from pyzbar.pyzbar import decode
from PIL import Image
import re

def decode_answer_key(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    
    if not decoded_objects:
        print("QR code not found")
        return None
    
    payload = decoded_objects[0].data.decode("utf-8")
    print(f"QR found: {payload}")
    
    answer_key = {"set": "", "part1": {}, "part2": {}}
    parts = payload.split("|")
    
    set_match = re.search(r"Set-(\w+)", parts[0])
    if set_match:
        answer_key["set"] = set_match.group(1)
    
    if len(parts) > 1:
        matches = re.findall(r"Q(\d+)=([A-D])", parts[1])
        for q_num, ans in matches:
            answer_key["part1"][f"Q{int(q_num):02d}"] = ans
    
    if len(parts) > 2:
        matches = re.findall(r"Q(\d+)=([A-D])", parts[2])
        for q_num, ans in matches:
            answer_key["part2"][f"Q{int(q_num):02d}"] = ans
    
    return answer_key

if __name__ == "__main__":
    image_path = "../samples/quiz sample.jpeg"
    result = decode_answer_key(image_path)
    if result:
        print("Answer Key:", result)