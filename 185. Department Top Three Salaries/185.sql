select d.Name Department, e1.Name Employee, e1.Salary Salary from Employee e1, Department D
where (select count(distinct(e2.Salary)) from Employee e2
        where e2.salary>e1.salary
        and e1.DepartmentId=e2.DepartmentId) < 3
and D.Id=e1.DepartmentId