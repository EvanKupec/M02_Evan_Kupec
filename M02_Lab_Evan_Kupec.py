"""
SDEV220
1-27-2024
Student: Evan Kupec
File Name: M02_Lab_Evan_Kupec.py
Description: This code asks for input of a students First and Last names,
and their GPA to determine if they qualify for the Dean's List or Honor Roll.
(It also properly capitalizes the text inputs)
"""
while True:
    print("--------------------")
    last_name = input("Enter the student's last name (enter 'ZZZ' to quit): ").strip().capitalize()

    if last_name == 'Zzz':
        print("Exiting the program")
        break

    first_name = input("Enter the student's first name: ").strip().capitalize()
    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll.")
