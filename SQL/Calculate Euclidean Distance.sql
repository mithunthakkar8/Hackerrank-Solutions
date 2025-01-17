select cast(sqrt(power(min(lat_N) - max(lat_N),2)
    + power(min(long_w) - max(long_w),2)) as decimal(36,4))
from station
