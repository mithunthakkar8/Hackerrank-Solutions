with lat_n_ranked as (
select lat_n
    , row_number() over (order by lat_n) rank
from station)
select cast(lat_n as decimal(36,4))
from lat_n_ranked
where rank = (select case when count(lat_n)%2=1 then ceiling(cast(count(lat_n) as float)/2)
            else count(lat_n)/2 end median_index from station)
