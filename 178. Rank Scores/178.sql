select s1.Score, (select count(distinct s2.Score) from Scores s2
                              where s2.Score>s1.Score) + 1 as Rank
from Scores s1 order by Rank;