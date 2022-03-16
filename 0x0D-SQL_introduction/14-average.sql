--  script that computes the score average of all records in the table second_table
SELECT SUM(score)/COUNT(id) AS average
FROM second_table
