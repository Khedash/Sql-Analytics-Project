
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1943@localhost/postgres')

# Step 2: Write your SQL query
query = """
SELECT 
    CASE 
        WHEN diabetes = 1 THEN 'Diabetic'
        ELSE 'Non-Diabetic'
    END AS diabetes_status,
    COUNT(*) AS num_patients
FROM diabetics_ds
GROUP BY diabetes_status
ORDER BY num_patients DESC;
"""

# Step 3: Read query result directly into Python
df = pd.read_sql(query, engine)

# Step 4: Visualize
plt.figure(figsize=(6,6))
plt.bar(df['diabetes_status'], df['num_patients'], color=['salmon', 'skyblue'])
plt.title('Diabetic vs Non-Diabetic Patients')
plt.ylabel('Number of Patients')
plt.xlabel('Diabetes Status')
plt.tight_layout()
plt.show()

