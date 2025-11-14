
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
        WHEN diabetics = 1 THEN 'Diabetic'
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



# Count number of diabetics (1) and non-diabetics (0) by gender
gender_counts = df.groupby(['Gender', 'diabetes']).size().unstack(fill_value=0)
gender_counts
# Create bar chart
gender_counts.plot(kind='bar', figsize=(7,5), color=['skyblue', 'salmon'])

# Add chart details
plt.title('Diabetes Prevalence by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Patients')
plt.xticks(rotation=0)
plt.legend(['Non-Diabetic', 'Diabetic'])
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save image
plt.tight_layout()
plt.savefig("assets/diabetes_gender.png")
plt.show()
