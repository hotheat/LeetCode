select d.Name Department, e.Name Employee, t1.maxSalary Salary from Employee e, Department d,
(select e1.DepartmentId, max(e1.Salary) maxSalary from Employee e1
group by e1.DepartmentId) as t1
where e.Salary=t1.maxSalary
and e.DepartmentId=t1.DepartmentId
and e.DepartmentId=D.Id