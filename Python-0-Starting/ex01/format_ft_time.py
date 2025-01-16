from datetime import date, time, datetime
from time import time

timeEpoch = time()
myDateTime = datetime.now()
myStringTime = myDateTime.strftime('%b %d %Y')

print("Seconds since January 1, 1970:", timeEpoch, "or", f"{timeEpoch:.2e} in scientific notation")

print(myStringTime)