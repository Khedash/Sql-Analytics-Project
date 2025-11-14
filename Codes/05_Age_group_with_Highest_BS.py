import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1943@localhost/postgres')

# Step 2: Write your SQL query
#5 Which age group has the highest average blood glucose?
Query =""" WITH AGE_GROUPS AS (
    SELECT 
        CASE WHEN AGE BETWEEN 0 AND 19 THEN '0-19'  
            WHEN AGE BETWEEN 20 AND 40 THEN '21-40' 
            WHEN AGE BETWEEN 41 AND 60 THEN '41-60'
            WHEN AGE BETWEEN 61 AND 80 THEN '61-80'  
            ELSE '81 +'
        END AS AGE_GROUP, 
        AVG(Blood_Glucose_Level) AS AVG_BGL
    FROM DIABETICS_db
    GROUP BY AGE_GROUP
)
SELECT *
FROM AGE_GROUPS
ORDER BY AVG_BGL DESC"""

#step 3: load into phyton
df = pd.read_sql(Query,engine)

# step 4 visualization
plt.figure(figsize=(6,5))
plt.bar(df['age_group'], df['avg_bgl'], color=['navy','lightblue'])
plt.xlabel('Age Groups')
plt.ylabel('Average Blood Glucose Level')
plt.title('Which age group has the highest average blood glucose?')
plt.tight_layout()
plt.show()