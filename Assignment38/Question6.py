import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

result = df.groupby("AssignmentCompleted")["FinalResult"].mean()

result.plot(kind="bar")

plt.title("Assignment Completed vs Final Result")
plt.xlabel("Assignment Completed")
plt.ylabel("Average Final Result")

plt.show() 