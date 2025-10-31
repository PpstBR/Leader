--QUERY exemplo_basico
SELECT TOP (:limit) * FROM Employees;

--QUERY outra_query
SELECT TOP (:limit) name, email FROM Customers;
