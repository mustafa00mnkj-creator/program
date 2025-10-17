# mustafa omar munam 
scores = [88, 92, 79, 85, 95 , 100]
def grade_calculator(scores):
    average = sum(scores) / len(scores)
    if 90 <= average <= 100:
        grade = "very good"
    elif 80 <= average < 90:
        grade = "good"
    elif 70 <= average < 80:
        grade = "fair"
    elif 60 <= average < 70:
        grade = "weak"
    else:
        grade = "fail"
    return average, grade
avg, letter = grade_calculator(scores)
print(f"المعدلل {avg}")
print(f"التقدير  {letter}")
