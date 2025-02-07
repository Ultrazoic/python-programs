import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
minute = int(time.strftime('%M'))
print(minute)
seconds = time.strftime('%S')
print(seconds)
if(hour<12 and hour>5):
    print("Good Morning Sir Have A Good Day")
elif(hour>12 and hour<18):
    print("Good Afternoon Sir")
elif(hour>18 and hour<22):
    print("Good Evening Sir ")
else:
    print("Good Night Sir Have A Good Sleep")