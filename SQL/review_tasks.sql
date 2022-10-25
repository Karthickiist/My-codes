use employees_mod;

select
	year(d.from_date) as year_,
	e.gender as gender,
    count(e.emp_no) as no_of_employees
from
	t_employees e
    join
    t_dept_emp d on d.emp_no=e.emp_no
group by year(d.from_date), gender
having year_>=1990
order by year_ ;