# STUDENT PERFORMANCE PREDICTion USING PYTHON PROGRAM

print("\t\tSTUDENT PERFORMANCE PREDICTION\n")

n = int(input("Enter the number of students : "))
data = []
first = 0
top_student = ""
top_grade = ""
#getting inputs of the student
for i in range(n):

    name = input("\nEnter name of the student : ")
    attendance = int(input("Enter attendance percentage : "))

    internal = int(input("Enter Internal Mark (out of 40) : "))
    external = int(input("Enter External Mark (out of 60) : "))

    score = internal + external
    #calculating grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "FAIL"

    data = data + [[i+1, name, attendance, internal, external, score, grade]]

    # FINDING THE TOP STUDENT
    if score > first:
        first = score
        top_student = name
        top_grade = grade

# DISPLAYING STUDENT DETAILS
print("\n")
print("Roll\tName\tAttendance\tInternal\tExternal\tTotal\tGrade")

for row in data:
    print(row[0], "\t", row[1], "\t", row[2], "%\t\t",
          row[3], "\t\t", row[4], "\t\t", row[5], "\t", row[6])

# PRINTING THE TOP STUDENT
print("\nHighest Score :", first, "/100")
print("Top Student :", top_student)
print("Grade :", top_grade)