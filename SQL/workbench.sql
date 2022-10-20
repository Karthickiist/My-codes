select distinct e1.*
from 
emp_manager e1
join 
emp_manager e2 on e1.emp_no=e2.manager_no;

create or replace view v_view as
 SELECT 
    emp_no, MAX(from_date) as from_date, MAX(to_date) as to_date
FROM
    dept_emp
GROUP BY emp_no;

create or replace view v_average as
select avg(s.salary)
from salaries s
join dept_manager d on s.emp_no=d.emp_no;



