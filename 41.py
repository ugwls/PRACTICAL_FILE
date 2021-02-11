# Inserting, projecting  and manipulating records – Insert, Select, Update, Delete
# (a)	Add 10 records in Emp table.
# (b)	Display all the records of Emp table.
# (c)	Increase all the salary of emp by 500.
# (d)	Delete all the employee details working in department no 50.

'''
a.
insert into employee(emp_id,emmp_name,age,phone_num,dept_id)
values(1,"ujjwal",18,1305240266,1),
values(2,"garvit",`13`,1125723767,1),
values(3,"mrk",24,0708474991,1),
values(4,"harsh",15,2377720050,1),
values(5,"muskan",13,0370602270,1),
values(6,"amrit",15,6051842944,1),
values(7,"sukarn",14,3411679960,1),
values(8,"shailaja",18,8698480510,1),
values(9,"akshay",17,0467788858,1),
values(10,"kashish",16,0467788858,1);
'''

'''
b. SELECT * from emp_table;
c. UPDATE emp_table SET salary= salary + 500;
d. DELETE from emp_table WHERE department_no = 50;
'''
