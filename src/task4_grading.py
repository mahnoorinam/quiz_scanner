def grade_student(student_answers, answer_key):
    """
    Student ke answers ko answer key se compare karke grade karta hai.
    """
    results = {
        "part1_score": 0,
        "part2_score": 0,
        "total_score": 0,
        "total_marks": 16,
        "percentage": 0,
        "grade": "",
        "details": []
    }

    # Part-I grading
    for q_num, correct_ans in answer_key["part1"].items():
        student_ans = student_answers["part1"].get(q_num, "")
        is_correct = student_ans == correct_ans
        if is_correct:
            results["part1_score"] += 1
        results["details"].append({
            "question": q_num,
            "part": "Part-I",
            "student_answer": student_ans,
            "correct_answer": correct_ans,
            "correct": is_correct
        })

    # Part-II grading
    for q_num, correct_ans in answer_key["part2"].items():
        student_ans = student_answers["part2"].get(q_num, "")
        is_correct = student_ans == correct_ans
        if is_correct:
            results["part2_score"] += 1
        results["details"].append({
            "question": q_num,
            "part": "Part-II",
            "student_answer": student_ans,
            "correct_answer": correct_ans,
            "correct": is_correct
        })

    # Total calculate karo
    results["total_score"] = results["part1_score"] + results["part2_score"]
    results["percentage"] = (results["total_score"] / results["total_marks"]) * 100

    # Grade assign karo
    p = results["percentage"]
    if p >= 90:
        results["grade"] = "A"
    elif p >= 80:
        results["grade"] = "B"
    elif p >= 70:
        results["grade"] = "C"
    elif p >= 60:
        results["grade"] = "D"
    else:
        results["grade"] = "F"

    return results


def print_result(student_info, results):
    print("\n" + "="*50)
    print(f"Student: {student_info['name']}")
    print(f"Reg#: {student_info['reg']}")
    print(f"Set: {student_info['set']}")
    print("-"*50)
    print(f"Part-I Score:  {results['part1_score']}/8")
    print(f"Part-II Score: {results['part2_score']}/8")
    print(f"Total Score:   {results['total_score']}/16")
    print(f"Percentage:    {results['percentage']:.1f}%")
    print(f"Grade:         {results['grade']}")
    print("="*50)


if __name__ == "__main__":
    # Test data — sample student answers
    answer_key = {
        "set": "C",
        "part1": {"Q01":"D","Q02":"A","Q03":"B","Q04":"A","Q05":"D","Q06":"A","Q07":"A","Q08":"B"},
        "part2": {"Q01":"C","Q02":"D","Q03":"D","Q04":"D","Q05":"C","Q06":"C","Q07":"C","Q08":"B"}
    }

    student_answers = {
        "part1": {"Q01":"D","Q02":"A","Q03":"B","Q04":"A","Q05":"D","Q06":"A","Q07":"A","Q08":"B"},
        "part2": {"Q01":"C","Q02":"D","Q03":"D","Q04":"D","Q05":"C","Q06":"C","Q07":"C","Q08":"B"}
    }

    student_info = {
        "name": "Mahnoor Inam",
        "reg": "BSE-FA24-020",
        "set": "C"
    }

    results = grade_student(student_answers, answer_key)
    print_result(student_info, results)