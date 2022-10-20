SELECT 
    *
FROM
    dept_manager_dup
ORDER BY dept_no;

SELECT 
    *
FROM
    department_dup
ORDER BY dept_no;

insert into department_dup(dept_name) value('public relation');

DELETE FROM department_dup 
WHERE
    dept_name = 'public relation';

alter table department_dup
modify dept_no varchar(50);

use employees;

SELECT 
    e.first_name, e.last_name, e.hire_date, t.title, d.dept_name
FROM
    employees e
        JOIN
    titles t ON e.emp_no = t.emp_no
        JOIN
    dept_manager dm ON e.emp_no = dm.emp_no
        JOIN
    departments d ON dm.dept_no = d.dept_no
WHERE
    t.title = 'Manager';

SELECT 
    e.first_name,
    e.last_name,
    e.hire_date,
    t.title,
    m.from_date,
    d.dept_name
FROM
    employees e
        JOIN
    dept_manager m ON e.emp_no = m.emp_no
        JOIN
    departments d ON m.dept_no = d.dept_no
        JOIN
    titles t ON e.emp_no = t.emp_no
WHERE
    t.title = 'Manager';
    
/*Average Salary*/

SELECT 
    d.dept_name, AVG(salary)
FROM
    departments d
        JOIN
    dept_manager dm ON dm.dept_no = d.dept_no
        JOIN
    salaries s ON s.emp_no = dm.emp_no
GROUP BY d.dept_name;

/*No of males and females*/
SELECT 
    e.gender, COUNT(e.gender)
FROM
    employees e
        JOIN
    titles t ON e.emp_no = t.emp_no
WHERE
    t.title = 'Manager'
GROUP BY gender;

/*create employee duplicate*/
drop table employees_dup;

CREATE TABLE employees_dup (
    emp_no INT(11),
    birth_date DATE,
    first_name VARCHAR(14),
    last_name VARCHAR(14),
    gender ENUM('M', 'F'),
    hire_date DATE
);

insert into employees_dup select * from employees
limit 20;

insert into employees_dup values('10001', '1953-09-02', 'Georgi', 'Fancelle',
'M', '1986-06-26');

/* union all */
SELECT 
    emp_no,
    first_name,
    last_name,
    NULL AS dept_no,
    NULL AS from_date
FROM
    employees_dup
WHERE
    last_name = 'Denis' 
UNION SELECT 
    NULL AS emp_no,
    NULL AS first_name,
    NULL AS last_name,
    dept_no,
    from_date
FROM
    dept_manager;
    
SELECT 
    first_name, last_name
FROM
    employees e
WHERE
    emp_no IN (SELECT 
            emp_no
        FROM
            dept_manager
        WHERE
            e.hire_date BETWEEN '1990-01-01' AND '1995-01-01');

/*exist and Non exist*/
SELECT 
    *
FROM
    employees e
WHERE
    EXISTS( SELECT 
            *
        FROM
            titles t
        WHERE
            e.emp_no = t.emp_no
                AND t.title = 'Assistant Engineer');

                
(select 
	e.emp_no as employee_id,
    min(d.dept_no) as department_id,
    (select
		emp_no
		from
			dept_manager 
		where emp_no=110022) as manager_id
	from
		employees e
        join
        dept_emp d on e.emp_no=d.emp_no
        where e.emp_no<10021
        group by e.emp_no
        order by e.emp_no)
union
(select 
	e.emp_no as employee_id,
    min(d.dept_no) as department_id,
    (select
		emp_no
		from
			dept_manager 
		where emp_no=110039) as manager_id
	from
		employees e
        join
        dept_emp d on e.emp_no=d.emp_no
        where e.emp_no>=10021
        group by e.emp_no
        order by e.emp_no
        limit 20)
union all
	(select 
	e.emp_no as employee_id,
    min(d.dept_no) as department_id,
    (select
		emp_no
		from
			dept_manager 
		where emp_no=110039) as manager_id
	from
		employees e
        join
        dept_emp d on e.emp_no=d.emp_no
        where e.emp_no=110022
        group by e.emp_no
        order by e.emp_no)
union all
	(select 
	e.emp_no as employee_id,
    min(d.dept_no) as department_id,
    (select
		emp_no
		from
			dept_manager 
		where emp_no=110022) as manager_id
	from
		employees e
        join
        dept_emp d on e.emp_no=d.emp_no
        where e.emp_no=110039
        group by e.emp_no
        order by e.emp_no);

create table emp_manager(
emp_no int(11) not null,
dept_no char(4) null,
manager_no int(11) not null
);

insert into emp_manager
((select 
	e.emp_no as employee_id,
    min(d.dept_no) as department_id,
    (select
		emp_no
		from
			dept_manager 
		where emp_no=110022) as manager_id
	from
		employees e
        join
        dept_emp d on e.emp_no=d.emp_no
        where e.emp_no<10021
        group by e.emp_no
        order by e.emp_no)
union
(select 
	e.emp_no as employee_id,
    min(d.dept_no) as department_id,
    (select
		emp_no
		from
			dept_manager 
		where emp_no=110039) as manager_id
	from
		employees e
        join
        dept_emp d on e.emp_no=d.emp_no
        where e.emp_no>=10021
        group by e.emp_no
        order by e.emp_no
        limit 20)
union all
	(select 
	e.emp_no as employee_id,
    min(d.dept_no) as department_id,
    (select
		emp_no
		from
			dept_manager 
		where emp_no=110039) as manager_id
	from
		employees e
        join
        dept_emp d on e.emp_no=d.emp_no
        where e.emp_no=110022
        group by e.emp_no
        order by e.emp_no)
union all
	(select 
	e.emp_no as employee_id,
    min(d.dept_no) as department_id,
    (select
		emp_no
		from
			dept_manager 
		where emp_no=110022) as manager_id
	from
		employees e
        join
        dept_emp d on e.emp_no=d.emp_no
        where e.emp_no=110039
        group by e.emp_no
        order by e.emp_no));
        
        

	

SELECT 
    *
FROM
    emp_manager;
SELECT 
    *
FROM
    dept_manager;
    
    
