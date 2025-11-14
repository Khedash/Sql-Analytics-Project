
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:1943@localhost/postgres')


query =""" SELECT 'Asian' AS race, 
       SUM(diabetics) AS diabetics_count,
       ROUND(SUM(diabetics)*100.0/COUNT(*),2) AS diabetes_prevalence_percentage
FROM DIABETICS_db
WHERE r_asian = 1
UNION ALL
SELECT 'AfricanAmerican', SUM(diabetics), ROUND(SUM(diabetics)*100.0/COUNT(*),2)
FROM DIABETICS_db
WHERE r_africanamerican = 1
UNION ALL
SELECT 'Caucasian', SUM(diabetics), ROUND(SUM(diabetics)*100.0/COUNT(*),2)
FROM DIABETICS_db
WHERE r_caucasian = 1
UNION ALL
SELECT 'Hispanic', SUM(diabetics), ROUND(SUM(diabetics)*100.0/COUNT(*),2)
FROM DIABETICS_db
WHERE r_hispanic = 1
UNION ALL
SELECT 'Other', SUM(diabetics), ROUND(SUM(diabetics)*100.0/COUNT(*),2)
FROM DIABETICS_db
WHERE r_other = 1
ORDER BY diabetes_prevalence_percentage DESC
"""
df = pd.read_sql(query,engine)

plt.figure(figsize=(7,5))
sns.barplot(x='diabetics_count', y='race', data=df, palette='Blues', orient='h')
plt.title('Which continent has the highest diabetic prevalance?')
plt.xlabel('Diabetic rate')
plt.ylabel('Race')
plt.tight_layout()
plt.show()
