# Creating and manipulating database and table structure in SQL – Create, Alter, Drop, Show and Describe.
# (a) Display all the available databases available in SQL.
# (b) Create database office and open it.
# (c) Display all the available tables of Office database.
# (d) Create a table Emp with following fields. Use appropriate constraints.
# Empno, Empname, Desig, Hiredate, Salary, Deptno
# (e) Add Mobile and Email field in table.
# (f) Remove Mobile field from the table.
# (g) Display the structure of Emp table.
# (h) Remove the Emp table structure and recreate it.

'''
a. SHOW DATABASES;
b. create database office;
use office;
c. show tables;
d. create table emp(
Empno int,
Empname varchar(30), 
Desig varchar(30), 
Hiredate date, 
Salary int, 
Deptno int )
e. ALTER TABLE emp
ADD Mobile int, email varchar(50);
f. ALTER TABLE emp
DROP COLUMN Mobile;
g. DESC emp;
h. DROP office.emp;
'''
