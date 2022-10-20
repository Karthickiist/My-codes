drop procedure if exists select_employees;
delimiter $$
create procedure select_employees()
begin
select * from employees limit 100;
end$$
delimiter ;

delimiter $$
create procedure average_salary()
begin
select emp_no,avg(salary) as Average_salary
from salaries;
end$$

delimiter $$
create procedure average_emp_salary(in p_emp_no int)
begin
select e.first_name, e.last_name, avg(s.salary) as salary_avg
from employees e
join 
salaries s on e.emp_no=s.emp_no
where e.emp_no=p_emp_no;
end$$

delimiter $$
create procedure emp_info(in v_first_name varchar(20), in v_last_name varchar(20), out v_emp_no int)
begin
select emp_no into v_emp_no
from employees
where
first_name=v_first_name and last_name=v_last_name;
end$$

set @p_emp_no=0;
call emp_info('Aruna', 'Journel', @p_emp_no);
select @p_emp_no;

/*Functions*/
delimiter $$
create function f_emp_info(v_first_name varchar(20), v_last_name varchar(20))returns date
DETERMINISTIC NO SQL READS SQL DATA
begin
declare v_max_from_date date;
declare v_salary decimal(10.2);
SELECT 
    MAX(s.from_date)
INTO v_max_from_date FROM
    salaries s
        JOIN
    employees e ON s.emp_no = e.emp_no
WHERE
    e.first_name = v_first_name
        AND e.last_name = v_last_name;
SELECT 
    s.salary
INTO v_salary FROM
    salaries s
        JOIN
    employees e ON s.emp_no = e.emp_no
WHERE
    e.first_name = v_first_name
        AND e.last_name = v_last_name
        AND s.from_date = v_max_from_date;
return v_salary;

end$$

SELECT F_EMP_INFO('Aruna', 'Journel')