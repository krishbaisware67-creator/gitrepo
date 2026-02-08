# Day 10: Mini Project - Student Grade Manager
# Apply everything you learned!

# Function to get student grades
def get_student_grades():
    students = {}
    
    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        
        grade = float(input(f"Enter {name}'s grade: "))
        students[name] = grade
    
    return students

# Function to calculate average
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades.values()) / len(grades)

# Function to find top student
def find_top_student(grades):
    if len(grades) == 0:
        return None
    return max(grades, key=grades.get)

# Function to display results
def display_results(students):
    print("\n=== Student Grades ===")
    for name, grade in students.items():
        if grade >= 90:
            status = "A - Excellent"
        elif grade >= 80:
            status = "B - Good"
        elif grade >= 70:
            status = "C - Average"
        else:
            status = "F - Needs Improvement"
        print(f"{name}: {grade} ({status})")
    
    avg = calculate_average(students)
    top = find_top_student(students)
    
    print(f"\nClass Average: {avg:.2f}")
    print(f"Top Student: {top}")

# Main program
print("=== Student Grade Manager ===")
students = get_student_grades()
display_results(students)

# Save to file
with open("grades.txt", "w") as file:
    file.write("Student Grades\n")
    file.write("=" * 20 + "\n")
    for name, grade in students.items():
        file.write(f"{name}: {grade}\n")

print("\nGrades saved to grades.txt!")

# TODO: Run this program and enter a few students
# See the results and check the grades.txt file
