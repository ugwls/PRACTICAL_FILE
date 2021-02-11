# Queries using DISTINCT, BETWEEN, IN, LIKE, IS NULL, ORDER BY, GROUP BY, HAVING

'''
b.SELECT Emp_name, Salary FROM Employee WHERE Salary BETWEEN 35000 AND 40000;
c.SELECT Emp_name FROM Employee WHERE city = 'Guwahati' or city = 'Surat' or city = 'Jaipur';
d.SELECT Emp_name FROM Employee WHERE Emp_name LIKE 'M%';
e.SELECT Emp_name FROM Employee WHERE department IS NULL;
f.SELECT * FROM employees e ORDER BY e.emp_id ASC;
g.SELECT department, AVG(salary) FROM employees GROUP BY department;
h.
'''
