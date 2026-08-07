import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

plt.scatter(df["SleepHours"], df["FinalResult"])

plt.title("Sleep Hours vs Final Result")
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")

plt.show()