-- Question 1.1
USE hospital_db;

SELECT COUNT(*) AS total_admissions
FROM admissions;

-- Question 1.2
SELECT AVG(DATEDIFF(discharge_date, admission_date)) AS average_length_of_stay
FROM admissions;

-- Question 2.1
SELECT primary_diagnosis, COUNT(*) AS total_admissions
FROM admissions
GROUP BY primary_diagnosis;

-- Question 2.2
SELECT service, AVG(DATEDIFF(discharge_date, admission_date)) AS average_length_of_stay
FROM admissions
GROUP BY service;

-- Question 3.1
SELECT discharge_disposition, COUNT(*) AS total_discharges
FROM discharges
GROUP BY discharge_disposition;

-- Question 3.2
SELECT service, COUNT(*) AS total_admissions
FROM admissions
GROUP BY service
HAVING total_admissions > 5;

-- Question 4.1
SELECT AVG(DATEDIFF(discharge_date, admission_date)) AS average_length_of_stay
FROM admissions
WHERE primary_diagnosis = 'Stroke';

-- Question 4.2
SELECT acuity, COUNT(*) AS total_visits
FROM ed_visits
GROUP BY acuity;

-- Question 5.1
SELECT primary_diagnosis, service, COUNT(*) AS total_admissions
FROM admissions
GROUP BY primary_diagnosis, service;

-- Question 5.2
SELECT MONTH(admission_date) AS month, COUNT(*) AS total_admissions
FROM admissions
GROUP BY MONTH(admission_date);

-- Bonus Question
SELECT service, 
       COUNT(*) AS total_admissions, 
       AVG(DATEDIFF(discharge_date, admission_date)) AS average_length_of_stay
FROM admissions
GROUP BY service
ORDER BY average_length_of_stay DESC;
