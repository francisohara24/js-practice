# Enter your code here. Read input from STDIN. Print output to STDOUT
from calendar import weekday

month, day, year = [int(i) for i in input().split()]
weekdays = {0: "MONDAY", 1: "TUESDAY", 2: "WEDNESDAY", 3: "THURSDAY", 4: "FRIDAY", 5: "SATURDAY", 6: "SUNDAY"}

answer = weekday(year, month, day)
print(weekdays[answer])