select p.Email from Person p group by p.Email
having count(*)>=2;