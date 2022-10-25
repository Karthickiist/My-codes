use employees_mod;
/*Task 1*/
select
year(d.from_date) as year_,
e.gender,
count(e.emp_no) as no_of_employees
from
t_employees e 
join
t_dept_emp d on e.emp_no=d.emp_no
where year(d.from_date)>=1990
group by e.gender,year_
order by year_;

use employees_mod;

/*Task 2*/
select
	d.dept_name,
    e.gender,
    dm.emp_no,
    dm.from_date,
    dm.to_date,
    ee.calander_year,
    case
		when ee.calander_year between year(dm.from_date) and year(dm.to_date)
        then 1 else 0
	end as activie
from
	(select
		year(hire_date) as calander_year
        from
			t_employees 
            group by calander_year) ee
	cross join
		t_dept_manager dm 
	join
		t_departments d on d.dept_no=dm.dept_no
	join
        t_employees e on e.emp_no=dm.emp_no;

select
	e.gender,
    d.dept_name,
    round(avg(s.salary),2) as salary,
    year(de.from_date) as calander_year
from
	t_dept_emp de
join
	t_employees e on de.emp_no=e.emp_no
join
	t_departments d on de.dept_no=d.dept_no
join
	t_salaries s on de.emp_no=s.emp_no
group by d.dept_no,e.gender,calander_year
having calander_year<=2002 and calander_year>=1990;

delimiter $$
create procedure avg_salary(in salary_max int , in salary_min int)
begin
select
	e.gender,
    d.dept_name,
    round(avg(s.salary),2) as salary,
    year(de.from_date) as calander_year
from
	t_dept_emp de
join
	t_employees e on de.emp_no=e.emp_no
join
	t_departments d on de.dept_no=d.dept_no
join
	t_salaries s on de.emp_no=s.emp_no
group by d.dept_no,e.gender,calander_year
having calander_year<=2002 and calander_year>=1990 and s.salary>=salary_min and s.salary<=salary_max;
end$$


drop procedure filter_salary;
