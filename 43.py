# Queries for Aggregate functions- SUM( ), AVG( ), MIN( ), MAX( ), COUNT( )
# a.	Find the average salary of the employees in employee table.
# b.	Find the minimum salary of a female employee in EMPLOYEE table.
# c.	Find the maximum salary of a male employee in EMPLOYEE table.
# d.	Find the total salary of those employees who work in Guwahati city.

'''
a. SELECT avg(salary) FROM employees;
b. SELECT MIN(salary) FROM employees;
c. SELECT MAX(salary) FROM employees;
d. SELECT SUM(salary) FROM employees WHERE city = 'Guwahati';
'''
