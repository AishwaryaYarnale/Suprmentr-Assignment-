# Student Data Manager

# Storing student data (Name: Marks)
students = {
    "Aishwarya": 85,
    "Rahul": 78,
    "Sneha": 92,
    "Kiran": 74,
    "Anjali": 88
}

# Finding topper
topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper])

# Calculating class average
total = sum(students.values())
average = total / len(students)
print("Class Average:", average)

# Assigning grades
print("\nGrades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "D"
    
    print(name, ":", grade)