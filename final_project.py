'''
School Management

Teacher:
1. Assign Student Grades
2. Assign Student Tasks
3. Assignment Summary
4. Mark Attendance
5. Get Student Profile
6. Switch Account

Student:
1. Look Up Assignments
2. Update Assignment Status
3. Check Attendance
4. Display Report Card
5. Switch Account
'''
from tabulate import tabulate
from datetime import date
import os
import time
accounts =[
    {
        "id": 10000,
        "name": "Jack",
        "age": 14,
        "date_of_birth": "01/15/08",
        "class": "class-12",
        "password": "student15",
        "role": "Student"
    },
    {
        "id": 50000,
        "name": "Jacob",
        "subject": "Mathematics",
        "password": "teacher12",
        "role": "Teacher"
    }
]
classes = {
    "class-12": [10000]
}
tasks = []
attendance = []
exams = []
reports = {}
exam_id_counter = 1
assignment_tracker = {}
student_id_counter = 10001
teacher_id_counter = 50001
task_id_counter = 1
application_name = "School Management"
main_options = """Options:
1. Sign Up
2. Sign In
3. Exit
"""
teacher_options = """Teacher Options:
1. Assign Student Grades
2. Assign Student Tasks
3. Assignment Summary
4. Mark Attendance
5. Get Student Profile
6. Switch Account
"""
student_options = """Student Options:
1. Look Up Assignments
2. Update Assignment Status
3. Check Attendance
4. Display Report Card
5. Switch Account
"""
while True:
    print(application_name + ":")
    print(main_options)
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Sign Up:")
            print("1. Student")
            print("2. Teacher")
            role_choice = int(input("Choose your role: "))
            if role_choice == 1:
                print("Student Sign Up:")
                student_id = student_id_counter
                student_id_counter += 1
                name = input("Name: ")
                age = int(input("Age: "))
                date_of_birth = input("Date of Birth(dd/mm/yyyy): ")
                student_class = input("Class: ").strip().lower()
                password = input("Password: ")
                account = {
                    "id": student_id,
                    "name": name,
                    "age": age,
                    "date_of_birth": date_of_birth,
                    "class": student_class,
                    "password": password,
                    "role": "Student"
                }
                accounts.append(account)
                if student_class in classes:
                    classes[student_class].append(student_id)
                else:
                    classes[student_class] = [student_id]
                print("Student account created successfully.")
                print(f"Your Student ID is: {student_id}")
            elif role_choice == 2:
                print("Teacher Sign Up:")
                teacher_id = teacher_id_counter
                teacher_id_counter += 1
                name = input("Name: ")
                subject = input("Subject: ")
                password = input("Password: ")
                account = {
                    "id": teacher_id,
                    "name": name,
                    "subject": subject,
                    "password": password,
                    "role": "Teacher"
                }
                accounts.append(account)
                print("Teacher account created successfully.")
                print(f"Your Teacher ID is: {teacher_id}")
            else:
                print("Invalid role choice.")
        case 2:
            while True:
                print("Sign In:")
                print("1. Student")
                print("2. Teacher")
                print("3. Return to Main Menu")
                role_choice = int(input("Choose your role: "))
                if role_choice == 1:
                    role = "Student"
                    user_id = int(input("Enter Student ID: "))
                    password = input("Enter Password: ")
                elif role_choice == 2:
                    role = "Teacher"
                    user_id = int(input("Enter Teacher ID: "))
                    password = input("Enter Password: ")
                elif role_choice == 3:
                    time.sleep(1)
                    os.system("clear")
                    break
                else:
                    role = None
                    print("Invalid role choice.")
                if role == None:
                    continue
                signed_in_account = None
                for account in accounts:
                    if (
                        account["id"] == user_id
                        and account["password"] == password
                        and account["role"] == role
                    ):
                        signed_in_account = account
                        break
                if signed_in_account == None:
                    print("Invalid ID or password.")
                    continue
                print("Sign in successful.")
                print(f"Welcome, {signed_in_account['name']}!")
                time.sleep(2)
                os.system("clear")
                switch_account = False
                if signed_in_account["role"] == "Teacher":
                    while True:
                        print(teacher_options)
                        teacher_choice = int(input("Enter your choice: "))
                        match teacher_choice:
                            case 1:
                                print("Assign Student Grades ")
                                print("1. Create Exam Record")
                                print("2. Enter Student Marks")
                                grade_choice = int(input("Enter your choice: "))
                                if grade_choice == 1:
                                    print("Create an Exam Record:")
                                    exam_id = exam_id_counter
                                    exam_id_counter += 1
                                    exam_name = input("Exam Name: ")
                                    number_of_subjects = int(input("Enter number of subjects: "))
                                    while number_of_subjects <= 0:
                                        print("Number of subjects must be greater than 0.")
                                        number_of_subjects = int(input("Enter number of subjects: "))
                                    subjects = []
                                    total_max_marks = 0
                                    for i in range(number_of_subjects):
                                        subject_name = input(f"Enter Subject-{i + 1} Name: ")
                                        max_marks = float(input(f"Enter Subject-{i + 1} Max Marks: "))
                                        while max_marks <= 0:
                                            print("Max marks must be greater than 0.")
                                            max_marks = float(input(f"Enter Subject-{i + 1} Max Marks: "))
                                        subject = {
                                            "name": subject_name,
                                            "max_marks": max_marks
                                        }
                                        subjects.append(subject)
                                        total_max_marks += max_marks
                                    exam = {
                                        "id": exam_id,
                                        "name": exam_name,
                                        "subjects": subjects,
                                        "max_marks": total_max_marks,
                                        "number_of_subjects": number_of_subjects
                                    }
                                    exams.append(exam)
                                    reports[exam_id] = []
                                    print("Exam record created successfully.")
                                    print(f"Exam ID: {exam_id}")
                                    print(f"Total Maximum Marks: {total_max_marks}")
                                elif grade_choice == 2:
                                    print("Enter Student Marks:")
                                    if len(exams) == 0:
                                        print("No exams have been created.")
                                    else:
                                        exam_rows = []
                                        for exam in exams:
                                            exam_rows.append([
                                                exam["id"],
                                                exam["name"],
                                                exam["number_of_subjects"],
                                                exam["max_marks"]
                                            ])
                                        exam_headers = [
                                            "Exam ID",
                                            "Exam Name",
                                            "Number of Subjects",
                                            "Maximum Marks"
                                        ]
                                        print(tabulate(exam_rows, headers=exam_headers, tablefmt="grid"))
                                        exam_id = int(input("Enter Exam ID: "))
                                        selected_exam = None
                                        for exam in exams:
                                            if exam["id"] == exam_id:
                                                selected_exam = exam
                                                break
                                        if selected_exam == None:
                                            print("Exam not found.")
                                        else:
                                            student_id = int(input("Enter Student ID: "))
                                            selected_student = None
                                            for account in accounts:
                                                if (account["id"] == student_id and account["role"] == "Student"):
                                                    selected_student = (account)
                                                    break
                                            if selected_student == None:
                                                print("Student not found.")
                                            else:
                                                marks_obtained = {}
                                                total_marks = 0
                                                for subject in selected_exam["subjects"]:
                                                    marks = float(input(f"Enter marks for {subject['name']} (0-{subject['max_marks']}): "))
                                                    while (marks < 0 or marks > subject["max_marks"]):
                                                        print("Invalid marks.")
                                                        marks = marks = float(input(f"Enter marks for {subject['name']} (0-{subject['max_marks']}): "))
                                                    marks_obtained[subject["name"]] = marks
                                                    total_marks += marks
                                                percentage = (total_marks / selected_exam["max_marks"]) * 100
                                                if percentage >= 90:
                                                    grade = "A"
                                                elif percentage >= 80:
                                                    grade = "B"
                                                elif percentage >= 70:
                                                    grade = "C"
                                                elif percentage >= 60:
                                                    grade = "D"
                                                else:
                                                    grade = "F"
                                                report = {
                                                    "student_id": student_id,
                                                    "marks_obtained": marks_obtained,
                                                    "total_marks": total_marks,
                                                    "grade": grade,
                                                    "percentage": percentage
                                                }
                                                existing_report = None
                                                for saved_report in reports[exam_id]:
                                                    if (saved_report["student_id"] == student_id):
                                                        existing_report = (saved_report)
                                                        break
                                                if existing_report == None:
                                                    reports[exam_id].append(report)
                                                    print("Student report created successfully.")
                                                else:
                                                    existing_report["marks_obtained"] = marks_obtained
                                                    existing_report["total_marks"] = total_marks
                                                    existing_report["grade"] = grade
                                                    existing_report["percentage"] = percentage
                                                    print("Student report updated successfully.")
                                                print(f"Total Marks: {total_marks}/{selected_exam['max_marks']}")
                                                print(f"Percentage: {percentage:.2f}%")
                                                print(f"Grade: {grade}")
                                else:
                                    print("Invalid choice.")
                            case 2:
                                print("Assign Student Task:")
                                title = input("Enter Title: ")
                                description = input("Enter Description: ")
                                task_class = input("Enter Class: ").strip().lower()
                                if task_class not in classes:
                                    print("That class does not exist.")
                                else:
                                    task_id = task_id_counter
                                    task_id_counter += 1
                                    task = {
                                        "id": task_id,
                                        "title": title,
                                        "description": description,
                                        "teacher_id":
                                            signed_in_account["id"],
                                        "teacher_name":
                                            signed_in_account["name"],
                                        "subject":
                                            signed_in_account["subject"],
                                        "class": task_class
                                    }
                                    tasks.append(task)
                                    assignment_tracker[task_id] = []
                                    print("Task assigned successfully.")
                                    print(f"Task ID: {task_id}")
                            case 3:
                                print("Assignment Summary:")
                                task_id = int(input("Enter Task ID: "))
                                selected_task = None
                                for task in tasks:
                                    if task["id"] == task_id:
                                        selected_task = task
                                        break
                                if selected_task == None:
                                    print("Task not found.")
                                else:
                                    task_class = (selected_task["class"])
                                    total_students = len(classes[task_class])
                                    if task_id in assignment_tracker:
                                        completed = len(assignment_tracker[task_id])
                                    else:
                                        completed = 0
                                    pending = (total_students - completed)
                                    rows = [
                                        [
                                            selected_task["id"],
                                            selected_task["title"],
                                            selected_task["class"],
                                            completed,
                                            pending
                                        ]
                                    ]
                                    headers = [
                                        "Task ID",
                                        "Title",
                                        "Class",
                                        "Completed",
                                        "Pending"
                                    ]
                                    print(tabulate(rows, headers=headers, tablefmt="grid"))
                            case 4:
                                print("Mark Attendance")
                                attendance_class = input("Enter Class: ").strip().lower()
                                if attendance_class not in classes:
                                    print("That class does not exist.")
                                else:
                                    print("Student IDs:", classes[attendance_class])
                                    entered_ids = input("Enter the present student IDs separated by commas: ")
                                    if entered_ids.strip() == "":
                                        present_ids = []
                                    else:
                                        present_ids = entered_ids.split(",")
                                        present_ids = list(map(int, present_ids))
                                        present_ids = list(set(present_ids))
                                    valid_present_ids = []
                                    invalid_ids = []
                                    for student_id in present_ids:
                                        if student_id in classes[attendance_class]:
                                            valid_present_ids.append(student_id)
                                        else:
                                            invalid_ids.append(student_id)
                                    absent_ids = []
                                    for student_id in classes[attendance_class]:
                                        if (student_id not in valid_present_ids):
                                            absent_ids.append(student_id)
                                    attendance_date = input("Enter Attendance Date (dd/mm/yyyy): ").strip()
                                    existing_record = None
                                    for record in attendance:
                                        if (record["date"] == attendance_date and record["class"] == attendance_class):
                                            existing_record = record
                                            break
                                    if existing_record == None:
                                        attendance_record = {
                                            "date": attendance_date,
                                            "class": attendance_class,
                                            "present": valid_present_ids,
                                            "absent": absent_ids,
                                            "teacher_id": signed_in_account["id"]
                                        }
                                        attendance.append(attendance_record)
                                    else:
                                        existing_record["present"] = (valid_present_ids)
                                        existing_record["absent"] = (absent_ids)
                                        existing_record["teacher_id"] = (signed_in_account["id"])
                                    rows = []
                                    for student_id in classes[attendance_class]:
                                        if (student_id in valid_present_ids):
                                            status = "Present"
                                        else:
                                            status = "Absent"
                                        rows.append([student_id,status])
                                    headers = ["Student ID", "Status"]
                                    print(tabulate(rows, headers=headers, tablefmt="grid"))
                                    print("Attendance recorded successfully.")
                                    if len(invalid_ids) > 0:
                                        print("Invalid student IDs:", invalid_ids)
                            case 5:
                                print("Get Student Profile:")
                                student_id = int(input("Enter Student ID: "))
                                selected_student = None
                                for account in accounts:
                                    if (account["id"] == student_id and account["role"] == "Student"):
                                        selected_student = account
                                        break
                                if selected_student == None:
                                    print("Student not found.")
                                else:
                                    rows = [
                                        [
                                            selected_student["id"],
                                            selected_student["name"],
                                            selected_student["age"],
                                            selected_student["date_of_birth"],
                                            selected_student["class"]
                                        ]
                                    ]
                                    headers = [
                                        "Student ID",
                                        "Name",
                                        "Age",
                                        "Date of Birth",
                                        "Class"
                                    ]
                                    print(tabulate(rows, headers=headers, tablefmt="grid"))
                            case 6:
                                print("Switching account...")
                                switch_account = True
                                break
                            case _:
                                print("Invalid choice.")
                        if teacher_choice != 6:
                            input("Press Enter to continue")
                            time.sleep(1)
                            os.system("clear")
                elif signed_in_account["role"] == "Student":
                    while True:
                        print(student_options)
                        student_choice = int(input("Enter your choice: "))
                        match student_choice:
                            case 1:
                                print("Your Assignments:")
                                student_class = (signed_in_account["class"])
                                rows = []
                                for task in tasks:
                                    if task["class"] == student_class:
                                        if (signed_in_account["id"] in assignment_tracker[task["id"]]):
                                            status = "Completed"
                                        else:
                                            status = "Pending"
                                        rows.append([
                                            task["id"],
                                            task["title"],
                                            task["description"],
                                            task["subject"],
                                            task["teacher_name"],
                                            status
                                        ])
                                headers = [
                                    "Task ID",
                                    "Title",
                                    "Description",
                                    "Subject",
                                    "Teacher",
                                    "Status"
                                ]
                                if len(rows) == 0:
                                    print("No assignments found for your class.")
                                else:
                                    print(tabulate(rows, headers=headers, tablefmt="grid"))
                            case 2:
                                print("Update Assignment Status:")
                                task_id = int(input("Enter Task ID: "))
                                selected_task = None
                                for task in tasks:
                                    if task["id"] == task_id:
                                        selected_task = task
                                        break
                                if selected_task == None:
                                    print("Task not found.")
                                elif (selected_task["class"] != signed_in_account["class"]):
                                    print("This task is not assigned to your class.")
                                elif (signed_in_account["id"] in assignment_tracker[task_id]):
                                    print("You already completed this task.")
                                else:
                                    assignment_tracker[task_id].append(signed_in_account["id"])
                                    print("Assignment marked as completed.")
                            case 3:
                                print("Check Attendance ")
                                student_id = signed_in_account["id"]
                                student_class = signed_in_account["class"]
                                rows = []
                                present_count = 0
                                total_days = 0
                                for record in attendance:
                                    if (record["class"] == student_class):
                                        total_days += 1
                                        if (student_id in record["present"]):
                                            status = "Present"
                                            present_count += 1
                                        else:
                                            status = "Absent"
                                        rows.append([record["date"], status])
                                if len(rows) == 0:
                                    print("No attendance records found.")
                                else:
                                    attendance_percentage = (present_count/ total_days) * 100
                                    headers = [
                                        "Date",
                                        "Status"
                                    ]
                                    print(tabulate(rows, headers=headers, tablefmt="grid"))
                                    print(f"Days Present: {present_count}")
                                    print(f"Total School Days: {total_days}")
                                    print(f"Attendance Percentage: {attendance_percentage:.2f}%")
                            case 4:
                                print("Display Report Card:")
                                student_id = signed_in_account["id"]
                                available_exams = []
                                for exam in exams:
                                    for report in reports[exam["id"]]:
                                        if (report["student_id"] == student_id):
                                            available_exams.append([
                                                exam["id"],
                                                exam["name"]
                                            ])
                                            break
                                if len(available_exams) == 0:
                                    print("No report cards are available.")
                                else:
                                    print(tabulate(available_exams, headers=["Exam ID", "Exam Name"], tablefmt="grid"))
                                    exam_id = int(input("Enter Exam ID: "))
                                    selected_exam = None
                                    for exam in exams:
                                        if exam["id"] == exam_id:
                                            selected_exam = exam
                                            break
                                    selected_report = None
                                    if selected_exam != None:
                                        for report in reports[exam_id]:
                                            if (report["student_id"] == student_id):
                                                selected_report = report
                                                break
                                    if (selected_exam == None or selected_report == None):
                                        print("Report card not found.")
                                    else:
                                        student_rows = [
                                            [
                                                signed_in_account["id"],
                                                signed_in_account["name"],
                                                signed_in_account["class"],
                                                selected_exam["name"]
                                            ]
                                        ]
                                        student_headers = [
                                            "Student ID",
                                            "Student Name",
                                            "Class",
                                            "Exam"
                                        ]
                                        print(tabulate(student_rows, headers=student_headers, tablefmt="grid"))
                                        subject_rows = []
                                        for subject in selected_exam["subjects"]:
                                            subject_name = subject["name"]
                                            subject_rows.append([
                                                subject_name,
                                                selected_report["marks_obtained"][subject_name],
                                                subject["max_marks"]
                                            ])
                                        subject_headers = ["Subject", "Marks Obtained", "Maximum Marks"]
                                        print(tabulate(subject_rows, headers=subject_headers, tablefmt="grid"))
                                        summary_rows = [[selected_report["total_marks"], selected_exam["max_marks"], f"{selected_report['percentage']:.2f}%", selected_report["grade"]]]
                                        summary_headers = ["Total Marks", "Maximum Marks", "Percentage", "Grade"]
                                        print(tabulate(summary_rows, headers=summary_headers, tablefmt="grid"))
                            case 5:
                                print("Switching account...")
                                switch_account = True
                                break
                            case _:
                                print("Invalid choice.")
                        if student_choice != 5:
                            input("Press Enter to continue")
                            time.sleep(1)
                            os.system("clear")
                if switch_account:
                    continue
                break
        case 3:
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Try again.")
    if choice != 3:
        input("Press Enter to continue")
        time.sleep(1)
        os.system("clear")
