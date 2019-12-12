from datetime import datetime

now = datetime.now()

current_time = now.strftime("%Y%m%d%H%M%S")
print("date and time =", current_time)	