'''
this is my solution to a programming problem.
basically, you had to calculate the minimum number of gates required for
a bunch of flights throughout the day.

'''

'''
if the arrival time of the next plane is before the departure time of the current plane then anther gate is needed.
the maximum number of overlapping flights is found and that is the maximum number of gates needed.
for example, if two flights overlap in the morning but three overlap in the after noon, three gates are needed, not two.
this is found by changing the starting point for the overlap search.
'''
arr = ['09:01','09:23','10:08','11:40','12:20','13:19','15:26','16:59']
dep = ['09:21','09:43','10:28','12:00','12:40','13:39','15:46','17:19']
print('Arrival times: ' + ', '.join(arr) + '\nDeparture times: ' + ', '.join(dep))
def convert(times):
    for a in range(len(times)):
        time = times[0].split(':')
        minutes = int(time[0])*60
        minutes += int(time[1])
        times.append(minutes)
        times.pop(0)
    return times
arr = convert(arr)
dep = convert(dep)
gates = []
for y in range(len(arr)-1):
    gates.append(1)
    x = 0
    run = True
    while run:
        if arr[x+1+y] < dep[x+y]:
            gates[y] += 1
            if len(arr) == x+2+y:
                run = False
        else:
            run = False
        x += 1
print('Number of gates needed:' , max(gates))
