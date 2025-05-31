import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

user_input = int(input('Write the number of goals you scored to know your market value: '))

goals = np.array([5, 10, 15, 20, 25]).reshape(-1, 1)
value = np.array([8, 12, 18, 22, 27])

df = pd.DataFrame({'goals': goals.flatten(), 'value (In Millions)': value})
print(df)

model = LinearRegression()
model.fit(goals, value)

m = model.coef_[0]
c = model.intercept_
mv_user = m * user_input + c
print(f"Predicted market value: {mv_user:.2f} million")

x_line = np.linspace(0, 30, 100).reshape(-1, 1)
y_line = model.predict(x_line)

plt.scatter(goals, value, color='red', label='Data Points')

plt.plot(x_line, y_line, color='blue', label=f'Fit Line: y = {m:.2f}x + {c:.2f}')

plt.scatter([user_input], [mv_user], color='green', s=100, label='Your Predicted Value', marker='x')

plt.title('Player Market Value Prediction')
plt.xlabel('Number of Goals Scored')
plt.ylabel('Value (In Millions)')
plt.legend()
plt.grid(True)
plt.show()
