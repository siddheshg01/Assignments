import pandas as pd

df = pd.read_csv("student_performance_ml.csv")


Ku = df.groupby("FinalResult")["StudyHours"].mean()
print(Ku)

if Ku[1] > Ku[0]:
    print("Higher study hours increase the passing rate.")
else:
    print("Study hours do not increase the passing rate.")

h = df.groupby("FinalResult")["Attendance"].mean()
print(h)

if h[1] > h[0]:
    print("Higher attendance improves the final result.")
else:
    print("Higher attendance does not improve the final result.")