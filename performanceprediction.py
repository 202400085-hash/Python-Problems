# STUDENT PERFORMANCE PREDICTOR USING PYTHON PROGRAM
print("\t\tSTUDENT PERFORMANCE PREDICTION\n")

n = int(input("Enter the number of students : "))
data = []
first = 0
top_student = ""
top_grade = ""

for i in range(n):

    name = input("\nEnter name of the student : ")
    attendance = int(input("Enter attendance percentage : "))
    score = int(input("Enter score percentage : "))

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

    data = data + [[i+1, name, attendance, score, grade]]

#FINDING THE TOP STUDENT
    if score > first:
        first = score
        top_student = name
        top_grade = grade

#ENTERING STUDENT DETAILS AS FILE
print("\n")
print("Roll\tName\tAttendance\tScore\tGrade")
for row in data:
    print( " ",row[0],  "\t",row[1], "\t" ,row[2], "%\t\t", row[3], "%\t", row[4])

#PRINTING THE TOP STUDENT
print("\nHighest Score :", first, "%")
print("Top Student :", top_student)
print("Grade :", top_grade)