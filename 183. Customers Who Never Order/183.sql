select c.Name as Customers from Customers c
where c.Id not in (select Orders.CustomerId from Orders)