from time import time
from datetime import datetime

ft_time = time()
ft_date = datetime.now()
month = ft_date.strftime('%b')

print(f"Seconds since January 1, 1970: {ft_time:,} \
or {ft_time:.2e} in scientific notation")

print(month, ft_date.day, ft_date.year)
