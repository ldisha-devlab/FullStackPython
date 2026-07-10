data=open("yuvraj.txt", "r")
strike_rates=[]

for line in data:
    columns=line.split()
    runs=int(columns[2])
    balls = int(columns[3])

    strike_rate=runs/balls *100

    strike_rates.append(strike_rate)

import statistics as st
deviation=st.stdev(strike_rates)
print("yuvraj deviation:", deviation)