import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

plt.scatter(df["StudyHours"], df["PreviousScore"])

plt.title("Study Hours vs Previous Scores")
plt.xlabel("Study Hours")
plt.ylabel("PreviousScores")

plt.show()


plt.boxplot(df["Attendance"])

plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")

plt.show()