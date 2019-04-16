select t.Request_at Day,
round(sum(case when t.Status like 'cancelled%' then 1 else 0 end
       ) / count(*), 2) as 'Cancellation Rate'
from Trips as t inner join Users as u
on t.Client_Id=u.Users_id and u.Banned='No'
where t.Request_at between '2013-10-01' and '2013-10-03'
group by t.Request_at