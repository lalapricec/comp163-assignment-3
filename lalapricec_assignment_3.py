# lalapricec_assignment_3.py
# COMP 163 - Assignment 4: College Life Adventure Game

# -------------------------------
# Step 1: Foundation Setup
# -------------------------------
student_name = "Lauren Price"   # Replace with your actual name
current_gpa = 3.2               # Float between 1.0 and 4.0
study_hours = 25                # Integer
social_points = 50              # Integer
stress_level = 60               # Integer 0–100

print("Welcome to the College Life Adventure Game!")
print(f"Student: {student_name}")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

# -------------------------------
# Step 2: Course Planning Decision
# -------------------------------
print("\nChoose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
choice = input("Your choice: ")

if choice == "A":
    if current_gpa <= 2.5:
        study_hours += 5
        stress_level -= 10
    else:
        study_hours += 3
        stress_level -= 5
elif choice == "B":
    study_hours += 5
    stress_level += 5
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 10
        stress_level += 15
    else:
        stress_level += 20
        current_gpa -= 0.2
else:
    print("Invalid choice.")

# -------------------------------
# Step 3: Study Strategy Decision
# -------------------------------
study_options = ["Programming", "Math", "English", "History"]

print("\nChoose a subject to focus on:")
for subject in study_options:
    print(f"- {subject}")

subject_choice = input("Your choice: ")

if subject_choice not in study_options:
    print("Invalid choice. Please pick a valid subject from the list.")
else:
    if subject_choice == "Programming" or subject_choice == "Math":
        current_gpa += 0.2
        study_hours += 5
        print(f"You studied {subject_choice}. GPA and study hours increased!")
    elif subject_choice == "English" and social_points < 60:
        current_gpa += 0.1
        social_points += 10
        print(f"You studied {subject_choice}. GPA slightly increased and social points improved!")
    else:
        current_gpa += 0.1
        print(f"You studied {subject_choice}. GPA slightly increased.")

# -------------------------------
# Step 4: Final Semester Assessment
# -------------------------------
print("\n--- Final Semester Assessment ---")

# Identity operator check
if type(current_gpa) is not int:  
    if current_gpa >= 3.5:
        if stress_level < 50:
            ending = "You excelled academically and maintained a healthy balance. Congrats!"
        else:
            ending = "Your grades are excellent, but stress took a toll. Take care!"
    elif current_gpa >= 2.5:
        if social_points >= 60:
            ending = "You managed average grades but enjoyed a vibrant social life."
        else:
            ending = "Average performance and low social life. Time to reflect!"
    else:
        ending = "You struggled academically. Consider adjusting your study habits."
else:
    ending = "Error: GPA type invalid."

print(ending)

# Show final stats
print("\nFinal Stats:")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")
