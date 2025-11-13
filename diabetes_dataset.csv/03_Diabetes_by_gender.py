import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1943@localhost/postgres')

# Step 2: Write your SQL query
# What is the diabetes prevalence by gender?
query = """ SELECT 
    Gender,
    COUNT(*) AS diabetic_count,
    ROUND( (COUNT(*) * 100.0) / (SELECT COUNT(*) FROM DIABETICS_db), 2) AS prevalence_percent
FROM DIABETICS_db
WHERE DIABETICS = 1
GROUP BY Gender
ORDER BY prevalence_percent DESC;"""

#step 3: load query int python
df = pd.read_sql(query,engine)

# step 4: Visualization
plt.figure(figsize=(5,3))
plt.bar(df['gender'], df['prevalence_percent'], color=['navy','lightblue'])
plt.title('Diabetes prevalence by gender')
plt.xlabel('Gender')
plt.ylabel('prevalence_percent')
plt.show()