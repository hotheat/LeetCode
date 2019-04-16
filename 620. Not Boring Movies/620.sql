select * from cinema c1
where (select count(*) from cinema c2 where c1.id<=c2.id) % 2 =1
and c1.description != 'boring'
order by rating desc