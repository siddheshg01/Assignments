import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

border = "-"*30
##############################################
#Step 1 : Load the Dataset.
##############################################

df = pd.read_csv("student_performance_ml.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)

df = pd.read_csv("student_performance_ml.csv")

total_students = len(df)
print("Total Students :", total_students)

passed_students = (df["FinalResult"] == 1).sum()
print("Passed Students :", passed_students)


failed_students = (df["FinalResult"] == 0).sum()
print("Failed Students :", failed_students)

Average_Studyhours= df["StudyHours"].mean()
print("Average_studyhour : ",Average_Studyhours)

Average_Attendence = df["Attendance"].mean()
print("Average Attendence :", Average_Attendence)

maximum_previousscore = df["PreviousScore"].max()
print("maximum_previousscore : ", maximum_previousscore)

minimum_sleephours = df["SleepHours"].min()
print("Minimun sleephours",minimum_sleephours)

print("minimun sleephours : ",df["SleepHours"].min())
