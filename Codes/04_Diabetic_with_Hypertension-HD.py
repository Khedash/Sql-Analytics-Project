import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1943@localhost/postgres')

# Step 2: Write your SQL query
#How many diabetic patients also have hypertension or heart disease?
Query = """SELECT 
   'Hypertension' as condition,COUNT(*) AS count
FROM DIABETICS_db
WHERE DIABETICS = 1 
  and Hypertension = 1 
 
UNION ALL 

SELECT 
   'Heart_Disease' as condition,COUNT(*) AS count
FROM DIABETICS_db
WHERE DIABETICS = 1 
  and heart_disease = 1;
"""

# step 3 load into python
df = pd.read_sql(Query,engine)

# step 4 Visualization
plt.figure(figsize=(5,3))
plt.bar(df['condition'], df['count'], color=['salmon', 'navy'])
plt.title('Diabetic Patients with Comorbidities')
plt.xlabel('Condition')
plt.ylabel('Number of Patients')
plt.tight_layout()
plt.show()