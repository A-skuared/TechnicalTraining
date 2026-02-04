from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Current date and time :- ", dt_string)


import sys
print(sys.version)
