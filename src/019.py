import calendar
start = 1901
end = 2000
sundayCount = 0
for year in range(start, end + 1):
    for month in range(1, 13):
        if calendar.monthrange(year, month)[0] == 6:
            sundayCount += 1
print sundayCount
