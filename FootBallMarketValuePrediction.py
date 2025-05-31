import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pyttsx3

'''
Coded with Love:
By Hardik Sharma Phuyal :D
'''

engine = pyttsx3.init()
text = "Enter Player's Name: "
engine.say(text)       
engine.runAndWait()
name = input("Enter Player's Name: ")

text = "Enter number of goals: "
engine.say(text)       
engine.runAndWait()
goals_input = int(input("Enter number of goals: "))

text = "Enter number of assists: "
engine.say(text)       
engine.runAndWait()
assists_input = int(input("Enter number of assists: "))

text = "Enter number of tackles: "
engine.say(text)       
engine.runAndWait()
tackles_input = int(input("Enter number of tackles: "))

text = "Enter pass accuracy (in %): "
engine.say(text)       
engine.runAndWait()
pass_accuracy = float(input("Enter pass accuracy (in %): "))

data = pd.read_csv('football_player_data.csv', encoding='latin1')

goals= data[['Goals']]
assists = data[['Assists']]
tackles = data[['Tackles']]
passAccuracy= data[['Pass Accuracy (%)']]
mv = data[['Market Value (in Millions)']]

X = data[['Goals', 'Assists', 'Tackles', 'Pass Accuracy (%)']]
y = data['Market Value (in Millions)'] 

model = LinearRegression()
model.fit(X,y)

m = model.coef_
c= model.intercept_
prediction = model.predict([[goals_input, assists_input, tackles_input, pass_accuracy]])

print(f"According to the Available data, your player {name}'s possible Market value should be {prediction} Million.")
text = f"According to the Available data, your player {name}'s possible Market value should be {prediction} Million."
engine.say(text)       
engine.runAndWait()