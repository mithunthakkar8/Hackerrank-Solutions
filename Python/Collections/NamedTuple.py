import sys
from collections import namedtuple

# Read the number of students (N). 
N = input()

# Read the column names (keys) which represent the attributes of each student.
keys = input().split()

# Define a namedtuple 'Student' with the given column names as fields (e.g., ID, Marks, Name, Class).
Student = namedtuple('Student', keys)

# Read the input data which contains student details (one per line).
data = sys.stdin.read()

# Split the input data into lines, where each line represents one student's details.
line_separated_data = data.splitlines()

# Initialize an empty list to store details of all students.
Student_Details = []

# Iterate over each line of student data.
for line in line_separated_data:
    # Split the line into individual attributes: ID, Marks, Name, and Class.
    ID, Marks, Name, Class = line.split()
    
    # Create a 'Student' namedtuple for each student using the extracted values and append to the list.
    Student_Details.append(Student(ID, Marks, Name, Class))

# Initialize a variable to calculate the total marks.
Total_Marks = 0

# Iterate over the list of students.
for Student_Iter in Student_Details:
    # Add each student's marks to the total marks (marks are converted to integers).
    Total_Marks += int(Student_Iter.MARKS)

# Calculate the total number of students.
Total_Students = int(N)

# Print the average marks by dividing the total marks by the total number of students.
print(Total_Marks / Total_Students)
