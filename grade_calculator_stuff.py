import numpy as np

current_grade = float(input("Enter current grade in class: "))
test_grade_string = str(input("Enter each test grade followed by a space or just enter the average grade of tests: "))
a = test_grade_string.split()
test_grade_list = [float(item) for item in a]

predicted_exam_grade = np.mean(test_grade_list)

def fgradecalc(exam_grade,semester_grade):
    fg = (exam_grade*0.20) + (semester_grade*0.80)
    return round(fg,2)

print(f"Your average test grade is {round(predicted_exam_grade,2)}")
print(f"Based on this your final grade will likely be {fgradecalc(predicted_exam_grade,current_grade)}")
print(f"If your teacher marks the final exam as a 0, then your final grade will be {fgradecalc(0.0,current_grade)}")
print(f"If you got a 50 on the final exam, your final grade would be would be {fgradecalc(50.0,current_grade)}")
print(f"If you got a 75 on the final exam, your final grade would be would be {fgradecalc(75.0,current_grade)}")
print(f"The highest your final grade could be is {fgradecalc(100.0,current_grade)}")