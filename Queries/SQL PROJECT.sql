--CREATE A TABLE FOR DIABETICS DATA SET

DROP TABLE if exists DIABETICS_db;

CREATE Table DIABETICS_db(
    Year int,
    Gender Varchar(6),
    Age int,
    Location Varchar(50),
    R_AfricanAmerican int,
    R_Asian int,
    R_Caucasian int,
    R_Hispanic int,
    R_Other int,
    Hypertension int,
    Heart_Disease int,
    Smoking_History Varchar(25),
    BMI numeric (4,2),
    hbA1c_Level numeric(2,1),
    Blood_Glucose_Level int,
    Diabetics int
);

Copy DIABETICS_db
from 'C:\Ayisha\diabetes_dataset.csv\diabetes_dataset.csv'
Delimiter ',' csv header

select * from DIABETICS_db
limit 10

----QUESTIONS------

--1 How many patients are diabetic vs non-diabetic?
SELECT 
    CASE WHEN DIABETICS = 1 THEN 'Diabetics' else 'Non_Diabetics'
    END AS Diabetics_status,
COUNT(*) as Num_Patients
from DIABETICS_db
GROUP by Diabetics
ORDER by Num_Patients DESC

--2 What is the average BMI by diabetes status

SELECT
    CASE WHEN DIABETICS = 1 THEN 'Diabetic' ELSE 'Non_Diabetic' END AS Diabetes_Status,
   ROUND(AVG(BMI),2) AS AVG_BMI
FROM DIABETICS_db
GROUP BY DIABETICS
ORDER BY AVG_BMI


--3  What is the diabetes prevalence by gender?

  SELECT 
    Gender,
    COUNT(*) AS diabetic_count,
    ROUND( (COUNT(*) * 100.0) / (SELECT COUNT(*) FROM DIABETICS_db), 2) AS prevalence_percent
FROM DIABETICS_db
WHERE DIABETICS = 1
GROUP BY Gender
ORDER BY prevalence_percent DESC;

--4 How many diabetic patients also have hypertension or heart disease?

SELECT 
    COUNT(*) AS diabetic_with_comorbidity
FROM DIABETICS_db
WHERE DIABETICS = 1 
  AND (Hypertension = 1 OR heart_disease = 1);

  SELECT 
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

SELECT 'Hypertension'as condition from DIABETICS_db

---5 Which age group has the highest average blood glucose?
WITH AGE_GROUPS AS (
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
ORDER BY AVG_BGL DESC


--6 Which locations have the most diabetic patients?

SELECT LOCATION, COUNT(DIABETICS) AS COUNT,ROUND( (COUNT(*) * 100.0) / 
(SELECT COUNT(*) FROM DIABETICS_db WHERE DIABETICS = 1), 2 ) AS percentage_of_diabetics
FROM DIABETICS_db
WHERE DIABETICS = 1
GROUP BY LOCATION
ORDER BY COUNT DESC
LIMIT 10

--7  * BMI categories vs diabetes status
WITH BMI_GROUPING AS (
    SELECT 
        CASE   
            WHEN BMI < 18.5 THEN 'UNDERWEIGHT'
            WHEN BMI BETWEEN 18.5 AND 24.9 THEN 'NORMAL'
            WHEN BMI BETWEEN 25 AND 29.9 THEN 'OVERWEIGHT'
            ELSE 'OBESE'
            END AS BMI_CATEGORY,DIABETICS 
    FROM DIABETICS_db
)
SELECT BMI_CATEGORY, DIABETICS, COUNT(*) AS DIABETICS_STATUS
FROM BMI_GROUPING
GROUP BY BMI_CATEGORY,DIABETICS
ORDER BY BMI_CATEGORY


SELECT
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
ORDER BY BMI_Category;

---highest continent

with CONTINENT AS (SELECT 'Asian' AS race, COUNT(*) AS total_people,
       SUM(diabetics) AS diabetics_count,
       ROUND(SUM(diabetics)*100.0/COUNT(*),2) AS diabetes_prevalence_percentage
FROM DIABETICS_db
WHERE r_asian = 1
UNION ALL
SELECT 'AfricanAmerican', COUNT(*), SUM(diabetics), ROUND(SUM(diabetics)*100.0/COUNT(*),2)
FROM DIABETICS_db
WHERE r_africanamerican = 1
UNION ALL
SELECT 'Caucasian', COUNT(*), SUM(diabetics), ROUND(SUM(diabetics)*100.0/COUNT(*),2)
FROM DIABETICS_db
WHERE r_caucasian = 1
UNION ALL
SELECT 'Hispanic', COUNT(*), SUM(diabetics), ROUND(SUM(diabetics)*100.0/COUNT(*),2)
FROM DIABETICS_db
WHERE r_hispanic = 1
UNION ALL
SELECT 'Other', COUNT(*), SUM(diabetics), ROUND(SUM(diabetics)*100.0/COUNT(*),2)
FROM DIABETICS_db
WHERE r_other = 1
ORDER BY diabetes_prevalence_percentage DESC
)
SELECT * FROM CONTINENT 
ORDER BY  diabetics_count DESC
limit 1




SELECT 
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

SELECT 'Hypertension'as condition from DIABETICS_db



SELECT 
    COUNT(*) AS total_people,
    SUM(CASE WHEN DIABETICS = 1 THEN 1 ELSE 0 END) AS diabetics_count,
    ROUND(
        SUM(CASE WHEN DIABETICS = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS diabetes_prevalence_percentage
FROM DIABETICS_db
ORDER BY total_people,diabetes_prevalence_percentage DESC