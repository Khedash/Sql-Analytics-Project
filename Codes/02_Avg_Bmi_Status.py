
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1943@localhost/postgres')

# Step 2: Write your SQL query
# What is the average BMI by diabetes status
query = """ SELECT
    CASE WHEN DIABETICS = 1 THEN 'Diabetic' ELSE 'Non_Diabetic' END AS Diabetes_Status,
   ROUND(AVG(BMI),2) AS AVG_BMI
FROM DIABETICS_db
GROUP BY DIABETICS
ORDER BY AVG_BMI """

#step 3: Read your query into python
df= pd.read_sql(query,engine)

# step 4: Visualize your query

plt.figure(figsize=(6,6))
plt.bar(df['diabetes_status'], df['avg_bmi'], color=['navy', 'lightblue'])
plt.title('Average BMI by Diabetes Status')
plt.xlabel('Diabetes Status')
plt.ylabel('Average BMI')
plt.tight_layout()
plt.show()