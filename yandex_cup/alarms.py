data = []
alarmTimes = []
with open("input.txt") as f:
    for line in f:
        for x in line.split():
            data.append(int(x))
f.close()
alarmTimes = data[3:]

alarmTimes = set(alarmTimes)
alarmTimes = list(alarmTimes)
alarmTimes.sort()

i = 0
while len(alarmTimes) < data[2] + data[0] - 1:
    if alarmTimes[i] + data[1] not in alarmTimes:
        alarmTimes.append(alarmTimes[i] + data[1])
        alarmTimes.sort()
    i+=1

with open("output.txt", 'w') as out:
    out.write(str(alarmTimes[data[2] - 1]))
out.close()