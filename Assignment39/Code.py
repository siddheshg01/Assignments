import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("student_performance_ml.csv")

print(df.head())
print(df.info())

# -----------------------------
# 2. Data Analysis
# -----------------------------
print("\nTotal Students :", len(df))
print(df["FinalResult"].value_counts())

print("\nAverage Study Hours")
print(df.groupby("FinalResult")["StudyHours"].mean())

print("\nAverage Attendance")
print(df.groupby("FinalResult")["Attendance"].mean())

# -----------------------------
# 3. Visualization
# -----------------------------

# Histogram
plt.hist(df["StudyHours"])
plt.title("Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.scatter(df["StudyHours"], df["PreviousScore"])
plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.show()

# Box Plot
plt.boxplot(df["Attendance"])
plt.title("Attendance")
plt.ylabel("Attendance")
plt.show()

# -----------------------------
# 4. Train Test Split
# -----------------------------
X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42)

# -----------------------------
# 5. Model Training
# -----------------------------
model = DecisionTreeClassifier()
model.fit(X_train,Y_train)

# -----------------------------
# 6. Prediction
# -----------------------------
Y_pred = model.predict(X_test)

print("\nActual\tPredicted")
for actual,pred in zip(Y_test,Y_pred):
    print(actual,"\t",pred)

# -----------------------------
# 7. Accuracy
# -----------------------------
accuracy = accuracy_score(Y_test,Y_pred)

print("\nAccuracy = {:.2f}%".format(accuracy*100))

# -----------------------------
# 8. Confusion Matrix
# -----------------------------
cm = confusion_matrix(Y_test,Y_pred)

print("\nConfusion Matrix")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]

print("True Positive :",TP)
print("True Negative :",TN)
print("False Positive :",FP)
print("False Negative :",FN)

# -----------------------------
# 9. Training Accuracy
# -----------------------------
train_pred = model.predict(X_train)

train_accuracy = accuracy_score(Y_train,train_pred)

print("\nTraining Accuracy = {:.2f}%".format(train_accuracy*100))

# -----------------------------
# 10. Testing Accuracy
# -----------------------------
print("Testing Accuracy = {:.2f}%".format(accuracy*100))

if train_accuracy > accuracy:
    print("Model is Overfitting")
elif train_accuracy < accuracy:
    print("Model is Underfitting")
else:
    print("Model is Well Fitted")

# -----------------------------
# 11. Compare max_depth
# -----------------------------
print("\nComparison of Different Depths")

for depth in [1,3,None]:
    dt = DecisionTreeClassifier(max_depth=depth,random_state=42)
    dt.fit(X_train,Y_train)

    pred = dt.predict(X_test)

    acc = accuracy_score(Y_test,pred)

    print("max_depth =",depth," Accuracy = {:.2f}%".format(acc*100))

# -----------------------------
# 12. Predict New Student
# -----------------------------
student = [[6,85,66,7,7]]

result = model.predict(student)

if result[0] == 1:
    print("\nPrediction : PASS")
else:
    print("\nPrediction : FAIL")

# -----------------------------
# 13. Conclusion
# -----------------------------
print("\nConclusion")
print("Decision Tree model successfully trained.")
print("Prediction completed.")
print("Accuracy calculated.")
print("Confusion matrix generated.")