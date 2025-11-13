from time import time
from datetime import datetime


print("Seconds since January 1, 1970:", "{:,.4f}".format(time()),
      "or", "{:.2e}".format(time()), "in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
