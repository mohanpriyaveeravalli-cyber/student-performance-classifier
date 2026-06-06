import joblib
import pandas as pd

model = joblib.load("best_model.pkl")

print("Enter Student Details")

study_hours = float(input("Study Hours: "))
attendance = float(input("Attendance (%): "))
assignment = float(input("Assignment Score: "))
previous_marks = float(input("Previous Marks: "))
participation = float(input("Participation (1-10): "))

student = pd.DataFrame({
    "StudyHours": [study_hours],
    "Attendance": [attendance],
    "AssignmentScore": [assignment],
    "PreviousMarks": [previous_marks],
    "Participation": [participation]
})

prediction = model.predict(student)

print(f"\nPredicted Category: {prediction[0]}")