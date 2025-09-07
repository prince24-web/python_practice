import time
hours = int(input('how many hour until your alarm?\n'))
minutes = int(input('How many minutes?\n'))
seconds = int(input('How many seconds?'))

hours = hours * 6
minutes = minutes * 6

total_time = hours + minutes + seconds 
time.sleep(total_time)
print('Timer up\n⏲️⌚⏰🔔')
