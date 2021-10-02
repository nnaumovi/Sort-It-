import os
import datetime as dt
redundant = []
past_day = dt.date(dt.date.today().year + (dt.date.today().month - 2) // 12, abs(dt.date.today().month - 2), dt.date.today().day)

directory = 'C:\Applications\\'
for filename in os.scandir(directory):
    fileobj = os.stat(filename)
    accessTime = os.path.getmtime(filename)
    if dt.date.fromtimestamp(accessTime) < past_day and 'Windows' not in os.path.basename(filename) and 'desktop' not in os.path.basename(filename) and 'assembl' not in os.path.basename(filename) and 'Microsoft' not in os.path.basename(filename):
        redundant.append(filename)

print("These applications have not been used in a while. Consider removing them to save memory!")
for elem in redundant:
    print(os.path.basename(elem))
