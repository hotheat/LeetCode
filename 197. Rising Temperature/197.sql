select w1.Id from Weather w1, Weather w2
where to_days(w1.RecordDate)-to_days(w2.RecordDate)=1
and w1.Temperature>w2.Temperature