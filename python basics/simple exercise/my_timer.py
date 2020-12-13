import os

secs=0
minit=0
hour=0
num2=0
buffer=0
while (secs <= 60):
    secs=secs+1
    if secs==60:
        minit=minit+1
        secs=0
    if minit==60:
        minit=0
        secs=0
        hour=hour+1
    if hour==2:
        hour=0
        minit=0
    os.system('cls')
    print (str(hour)+":"+str(minit)+":"+str(secs))
    for num2 in range(1000):
        buffer=buffer+1
