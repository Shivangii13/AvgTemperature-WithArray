
# calculate Average Temperture
numDays = int(input("how many day's temperature"))
total = 0
for i in range (1, numDays+1):
    nextDay = int(input("Day" + str(i) + "'s high temp"))
    total += nextDay

avg = round(total/numDays,2)
print("\nAverage = " + str(avg))

#Days above average temperature
numDays = int(input("how many day's temperature"))
total = 0
temp = []
for i in range (numDays):
    nextDay = int(input("Day" + str(i+1) + "'s high temp"))
    temp.append(nextDay)
    total += temp[i]

avg = round(total/numDays,2)
print("\nAverage = " + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1
print(str(above) + "day(s) above average")
