import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('diabetes_prediction_dataset.csv')

age_input = int(input('Write Your age: '))
weight_input = int(input('Write Your Weight: '))
exercise_input = int(input('Write How many Times You exercise in a week: '))
bmi_input = int(input('Write your BMI: '))
diet = int(input('Write your diet, 1 for non Veg and 0 for veg: '))

x_data = data[['Age','Weight (kg)','BMI','Exercise per Week','Diet (1=Non-Veg, 0=Veg)']]
y_data = data['Diabetes in 5 Years (1=Yes, 0=No)']

model = LogisticRegression()
model.fit(x_data, y_data)

input_data = [[age_input, weight_input, bmi_input, exercise_input, diet]]

prediction = model.predict(input_data)
probabilities = model.predict_proba(input_data)

print(f"\nPrediction: {'Diabetes' if prediction[0] == 1 else 'No Diabetes'}")

if prediction[0] == 1:
    print(f"Probability of Diabetes: {probabilities[0][1] * 100:.2f}%")
else:
    print(f"Probability of No Diabetes: {probabilities[0][0] * 100:.2f}%")
