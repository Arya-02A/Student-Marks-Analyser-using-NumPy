import numpy as np

# Sample student names and their marks in 3 subjects Data.
students = ["Ram", "Lakshman", "Bharat", "Shatrugna"]
marks = np.array([
    [85, 90, 95],    # Ram
    [78, 80, 82],    # Lakshman
    [92, 88, 84],    # Bharat
    [70, 75, 80]     # Shatrugna
])

# Total marks for each student
total_marks = np.sum(marks, axis=1)

# Average marks for each student
average_marks = np.mean(marks, axis=1)

# Highest marks among all of the students
highest_marks = np.max(marks, axis=1)

# Lowest marks among all students
lowest_marks = np.min(marks, axis=1)

# Display Results
for i in range(len(students)):
    print(f"{students[i]} - Total: {total_marks[i]}, Average: {average_marks[i]:.2f}, Highest: {highest_marks[i]}, Lowest: {lowest_marks[i]}")
