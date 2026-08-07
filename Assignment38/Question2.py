import pandas as pd

df = pd.read_csv("student_performance_ml.csv")


result = df["FinalResult"].value_counts()

print(result)


passed = result[1]
failed = result[0]


total = len(df)


passed_percentage = (passed / total) * 100
failed_percentage = (failed / total) * 100

print("Passed Students :", passed)
print("Failed Students :", failed)

print("Passed Percentage : {:.2f}%".format(passed_percentage))
print("Failed Percentage : {:.2f}%".format(failed_percentage))


if abs(passed_percentage - failed_percentage) <= 10:
    print("Dataset is Balanced")
else: 
    print("Dataset is Imbalanced")