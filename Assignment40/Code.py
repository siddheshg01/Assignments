import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("student_performance_ml.csv")

# Features and Target
X = df[["StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"]]

Y = df["FinalResult"]

# Train-Test Split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

# ===============================
# Question 1
# Feature Importance
# ===============================

print("Feature Importance\n")

importance = model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(feature, ":", score)

print("\nMost Important Feature :", X.columns[importance.argmax()])
print("Least Important Feature :", X.columns[importance.argmin()])


# ===============================
# Question 2
# Remove SleepHours
# ===============================

print("\nAccuracy After Removing SleepHours")

X2 = df.drop(columns=["SleepHours", "FinalResult"])

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
    X2, Y, test_size=0.2, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)

model2.fit(X_train2, Y_train2)

pred2 = model2.predict(X_test2)

acc2 = accuracy_score(Y_test2, pred2)

print("Accuracy :", acc2 * 100)


# ===============================
# Question 3
# Only StudyHours & Attendance
# ===============================

print("\nOnly StudyHours and Attendance")

X3 = df[["StudyHours", "Attendance"]]

X_train3, X_test3, Y_train3, Y_test3 = train_test_split(
    X3, Y, test_size=0.2, random_state=42
)

model3 = DecisionTreeClassifier(random_state=42)

model3.fit(X_train3, Y_train3)

pred3 = model3.predict(X_test3)

acc3 = accuracy_score(Y_test3, pred3)

print("Accuracy :", acc3 * 100)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("student_performance_ml.csv")

# Features and Target
X = df[["StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"]]

Y = df["FinalResult"]

# Train-Test Split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

# ===============================
# Question 1
# Feature Importance
# ===============================

print("Feature Importance\n")

importance = model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(feature, ":", score)

print("\nMost Important Feature :", X.columns[importance.argmax()])
print("Least Important Feature :", X.columns[importance.argmin()])


# ===============================
# Question 2
# Remove SleepHours
# ===============================

print("\nAccuracy After Removing SleepHours")

X2 = df.drop(columns=["SleepHours", "FinalResult"])

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
    X2, Y, test_size=0.2, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)

model2.fit(X_train2, Y_train2)

pred2 = model2.predict(X_test2)

acc2 = accuracy_score(Y_test2, pred2)

print("Accuracy :", acc2 * 100)


# ===============================
# Question 3
# Only StudyHours & Attendance
# ===============================

print("\nOnly StudyHours and Attendance")

X3 = df[["StudyHours", "Attendance"]]

X_train3, X_test3, Y_train3, Y_test3 = train_test_split(
    X3, Y, test_size=0.2, random_state=42
)

model3 = DecisionTreeClassifier(random_state=42)

model3.fit(X_train3, Y_train3)

pred3 = model3.predict(X_test3)

acc3 = accuracy_score(Y_test3, pred3)

print("Accuracy :", acc3 * 100)

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# ===============================
# Question 7
# Compare Different Random States
# ===============================

print("\nComparison of Different Random States")

for i in [0, 10, 42]:

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=i
    )

    model = DecisionTreeClassifier(random_state=i)

    model.fit(X_train, Y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(Y_test, pred)

    print("Random State =", i, " Accuracy =", acc * 100)


# ===============================
# Question 8
# Visualize Decision Tree
# ===============================

plt.figure(figsize=(20,10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Fail", "Pass"],
    filled=True
)

plt.title("Decision Tree")
plt.show()


# ===============================
# Question 9
# Create PerformanceIndex Feature
# ===============================

df["PerformanceIndex"] = (
    df["StudyHours"] +
    df["Attendance"] +
    df["PreviousScore"]
)

print("\nPerformanceIndex Added Successfully")

X_new = df.drop(columns=["FinalResult"])

Y_new = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X_new, Y_new, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

pred = model.predict(X_test)

acc = accuracy_score(Y_test, pred)

print("Accuracy after adding PerformanceIndex :", acc * 100)


# ===============================
# Question 10
# Training Accuracy vs Testing Accuracy
# ===============================

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

train_acc = accuracy_score(Y_train, train_pred)
test_acc = accuracy_score(Y_test, test_pred)

print("\nTraining Accuracy :", train_acc * 100)
print("Testing Accuracy :", test_acc * 100)

if train_acc == 1 and test_acc < train_acc:
    print("\nModel is Overfitting")
elif train_acc < test_acc:
    print("\nModel is Underfitting")
else:
    print("\nModel is Well Fitted")


# ===============================
# Conclusion
# ===============================

print("\nConclusion")
print("1. Feature importance identifies the most useful features.")
print("2. Removing important features may reduce accuracy.")
print("3. Using fewer features generally reduces model performance.")
print("4. Decision Tree predicts student performance successfully.")
print("5. Training accuracy is usually higher than testing accuracy.")
print("6. A large gap between training and testing accuracy indicates overfitting.")