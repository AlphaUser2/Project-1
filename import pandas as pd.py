import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load data
df = pd.read_csv('C:/Users/santh/Desktop/DATASET/titanic.csv')

# Display first few rows
print(df.head())

# Summary statistics
print(df.describe())

# Handle missing values
df.fillna(method='ffill', inplace=True)

# Distribution of Age
sns.histplot(df['Age'].dropna(), kde=True,)
plt.title('distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()



