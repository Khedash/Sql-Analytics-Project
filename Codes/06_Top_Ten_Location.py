import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1943@localhost/postgres')

# Run your SQL query
query = """
SELECT LOCATION, COUNT(DIABETICS) AS count, ROUND((COUNT(*) * 100.0) / 
(SELECT COUNT(*) FROM DIABETICS_db WHERE DIABETICS = 1), 2) AS percentage_of_diabetics
FROM DIABETICS_db
WHERE DIABETICS = 1
GROUP BY LOCATION
ORDER BY count DESC
LIMIT 10
"""
df = pd.read_sql(query, engine)

# Create vertical bar plot
plt.figure(figsize=(8,6))  # Adjust figure size
sns.barplot(x='count', y='location', data=df, palette='Blues', orient='h')  # horizontal bars

# Add labels
plt.xlabel("Number of Diabetics")
plt.ylabel("Location")
plt.title("Top 10 Locations by Number of Diabetics")

# Show percentages on bars
for index, row in df.iterrows():
    plt.text(row['count'] + 0.5, index, f"{row['percentage_of_diabetics']}%", va='center')

plt.tight_layout()
plt.show()



