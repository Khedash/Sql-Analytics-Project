import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:1943@localhost/postgres')

query = """SELECT
    BMI_Category,
    SUM(CASE WHEN DIABETICS = 1 THEN 1 ELSE 0 END) AS diabetic_count,
    SUM(CASE WHEN DIABETICS = 0 THEN 1 ELSE 0 END) AS non_diabetic_count
FROM (
    SELECT
        CASE 
            WHEN BMI < 18.5 THEN 'Underweight'
            WHEN BMI BETWEEN 18.5 AND 24.9 THEN 'Normal'
            WHEN BMI BETWEEN 25 AND 29.9 THEN 'Overweight'
            ELSE 'Obese'
        END AS BMI_Category,
        DIABETICS
    FROM DIABETICS_db
) AS grouped
GROUP BY BMI_Category
ORDER BY BMI_Category;"""

# Step 3: Load query result
df = pd.read_sql(query, engine)

# Step 4: Visualization
plt.figure(figsize=(6,4))
plt.bar(df['bmi_category'], df['diabetic_count'], color='royalblue')
plt.title('Diabetic Patients Across BMI Categories')
plt.xlabel('BMI Category')
plt.ylabel('Number of Diabetic Patients')
plt.tight_layout()
plt.show()
