import numpy as np
import matplotlib as plt


grade_list = []

def fsg(semester_grade_1,semester_grade_2, exam_grade,sem_num): # fsg stands for first semester grade.
    if sem_num == 1:
        return round(((semester_grade_1*0.8) + (exam_grade*0.2)),2)
    elif sem_num == 2:
        return round(((semester_grade_1*0.4) + (semester_grade_2*0.4) + (exam_grade*0.2)),2)

s_num = int(input("Do you want to calculate grade after final exam (enter 1) or midterm (enter 2)?: "))
if s_num == 1:
    secq_grade = float(input("Please enter your current 2nd quarter grade: "))
    test_numbers = int(input("How many tests have you taken this semester?: "))
    for i in range(test_numbers):
        test_grade = float(input(f"Please input numerical grade for test number {i+1}: "))
        grade_list.append(test_grade)
    test_grade_average = np.mean(grade_list)
    print(f"Your current grade is a {secq_grade}.")
    print(f"Based on previous test grades, your average test grade is a {round(test_grade_average,2)}.")
    print(f"Following this trajectory, your first semester grade would probably be a {round(fsg(secq_grade,0,test_grade_average,1),2)}.")
    print(f"The maximum grade you could have in the class at the end of the first semester would be a {round(fsg(secq_grade,0,100.0,1),2)}.")
    print(f"If you got a 0 on the exam your grade in the class at the end of the first semester would be a {round(fsg(secq_grade,0,0,1),2)}.")
elif s_num == 2:
    sem_grade_1 = float(input("Please enter your 1st semester grade: "))
    forq_grade = float(input("Please enter your current 4th quarter grade: "))
    test_numbers = int(input("How many tests have you taken this semester?: "))
    for i in range(test_numbers):
        test_grade = float(input(f"Please input numerical grade for test number {i+1}: "))
        grade_list.append(test_grade)
    test_grade_average = np.mean(grade_list)
    print(f"Your current grade is a {forq_grade}.")
    print(f"Based on previous test grades, your average test grade is a {round(test_grade_average,2)}.")
    print(f"Following this trajectory, your final grade would probably be a {fsg(forq_grade,sem_grade_1,test_grade_average,2)}.")
    print(f"The maximum final grade you could have in the class would be a {fsg(forq_grade,sem_grade_1,100.0,2)}.")
    print(f"If you got a 0 on the exam your final grade in the class would be a {fsg(forq_grade,sem_grade_1,0,2)}.")


