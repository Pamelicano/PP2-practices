from datetime import *

# TASK 1: Write a Python program to subtract five days from current date.
cur = date.today()
print(cur - timedelta(days=5))

# TASK 2: To print yesterday, today and tomorrow.
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday, "Today:", today, "Tomorrow:", tomorrow)

# TASK 3: Write a Python program to drop microseconds from datetime.
now = datetime.now()
print("Current datetime:", now)
print("Datetime without microseconds:", now.replace(microsecond=0))

# TASK 4: Write a Python program to calculate two date difference in seconds.
date1 = date.today()
date2 = date1 + timedelta(days=5)
difference = date2 - date1
print("Difference in seconds:", difference.total_seconds())