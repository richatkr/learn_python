# Module is reuse codes and functionality written by someone else. Exa of Standard module available in python is
# math module, calender module etc 
import math
print(math.sqrt(16)," ", math.pow(2,5), math.log10(1000), math.pi)

# to get all the available function in a module
print(dir(math))

import calendar
print(calendar.month(2022,1), calendar.isleap(2022), calendar.isleap(2024))
print(dir(calendar))

# you can create your own module also
