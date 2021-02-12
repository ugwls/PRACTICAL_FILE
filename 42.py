# Queries using DISTINCT, BETWEEN, IN, LIKE, IS NULL, ORDER BY, GROUP BY, HAVING
# (a)	Display the number of departments. Each department should be displayed once.
# (b)	Find the name and salary of those employees whose salary is between 35000 and 40000.
# (c)	Find the name of those employees who live in guwahati, surat or jaipur city.
# (d)	Display the name of those employees whose name starts with ‘M’.
# (e)	List the name of employees not assigned to any department.
# (f)	Display the list of employees in descending order of employee code.
# (g)	Find the average salary at each department.
# (h)	Find maximum salary of each department and display the name of that department 
#       which has maximum salary more than 39000.


'''
b.SELECT Emp_name, Salary FROM Employee WHERE Salary BETWEEN 35000 AND 40000;
c.SELECT Emp_name FROM Employee WHERE city = 'Guwahati' or city = 'Surat' or city = 'Jaipur';
d.SELECT Emp_name FROM Employee WHERE Emp_name LIKE 'M%';
e.SELECT Emp_name FROM Employee WHERE department IS NULL;
f.SELECT * FROM employees e ORDER BY e.emp_id ASC;
g.SELECT department, AVG(salary) FROM employees GROUP BY department;
h.
'''
