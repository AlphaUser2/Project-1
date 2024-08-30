import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('C:/Users/santh/Desktop/DATASET/titanic.csv')

print(data.head(10))

total_passengers = data['PassengerId'].count()
print(f"Total number of passengers: {total_passengers}")

surviors = data['Survived'].sum()
print(f"Total number of Surviors: {surviors}")

survival_rate = (surviors / total_passengers) * 100
print(f"Survival rate: {survival_rate:.2f}%")

# Count the number of survivors and non-survivors
survival_counts = data['Survived'].value_counts()

# Plot the data
plt.figure(figsize=(8, 6))
plt.bar(survival_counts.index, survival_counts.values, color=['red', 'green'])
plt.xlabel('Survived')
plt.ylabel('Count')
plt.title('Number of Survivors vs. Non-Survivors')
plt.xticks([0, 1], ['Not Survived', 'Survived'])
plt.show()


