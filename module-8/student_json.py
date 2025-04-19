import json

# Function to print student list
def print_students(students, message):
    print(message)
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")
    print()

# Update this path if needed
file_path = "student.json"

# Load original data from JSON file
with open(file_path, "r") as file:
    student_list = json.load(file)

# Print original student list
print_students(student_list, "Original Student List:")

# Add your information here
new_student = {
    "F_Name": "Brijette",          # Replace with your first name
    "L_Name": "Baboolal",           # Replace with your last name
    "Student_ID": 67318,       # Replace with your fictional ID
    "Email": "happy_happy@gmail.com" # Replace with your fictional email
}
student_list.append(new_student)

# Print updated student list
print_students(student_list, "Updated Student List (after adding your info):")

# Save updated list back to the JSON file
with open(file_path, "w") as file:
    json.dump(student_list, file, indent=4)

print("The student.json file has been updated.")