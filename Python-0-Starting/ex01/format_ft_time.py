from datetime import datetime
import time

sec = time.time()
date = datetime.now().strftime("%b %d %Y")

print (f"Seconds since January 1, 1970: {sec:,.4f} or {sec:.2e} in scientific notation")
print (date)
