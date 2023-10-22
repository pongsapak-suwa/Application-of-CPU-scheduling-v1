# Application-of-CPU-scheduling-v1
- [x] [Non-preemptive Longest Job First](#Non-preemptive-Longest-Job-First) <br />
- [x] [Preemptive Longest Job First](#Then-like-preemptive-Longest-Job-First?) <br />
- [x] [RR ( Round Robin ) ](#and-last-RR-(-Round-Robin-))
---
>Comput
> * CPU utilization, <br />
> * Throughput, <br />
> * Turnaround time of each process, <br />
> * Avg Turnaround time , <br />
> * Waiting time of each process, <br />
> * Avg Waiting time <br /><br /><br />
        Note1: Input will be provided in excel or CSV file forma <br />
---
---
- [x]  use import pandas as pd install pandas in terminal :<br />
```
pip install pandas
```
- [x]  use import tkinter as tk install Tkinter in terminal :<br />
```
pip install tk
```
- [x]  use import numpy as np install numpy in terminal :<br />
```
pip install numpy
```
- [x]  use import matplotlib.pyplot as plt install numpy in terminal :<br />
```
pip install matplotlib
```

--- 
# Non-preemptive Longest Job First <br />
main funtion algorithm :
```
while(succeed_process < max_data):
    if outside_process != []:
        for inum in list(outside_process):         
            if inum[2] <= current_time :
                interesting_process.append(inum)       
                outside_process.remove(inum)          
                
    if len(interesting_process) >= 1:                
        longest_burst_time(interesting_process)
        process_suv(succeed_process,current_time,working_process)
            
        current_time += working_process[succeed_process][1]
        succeed_process += 1

    elif (interesting_process == [])and (outside_process != []):
        current_time += 1
```
funtion Check it and pull it out the longest process inside :
```
def longest_burst_time(interesting_process):        
    if len(interesting_process) > 1 :
        interesting_process.sort(key=lambda i:i[1])   
    
    working_process.append(interesting_process.pop())   

    return working_process
```
funtion convert data process :
```
def process_suv(succeed_process,current_time,working_process): #more finished program
    finished_program.append([])
    finished_program[succeed_process].append(working_process[succeed_process][0]) 
    finished_program[succeed_process].append(current_time)                        
    finished_program[succeed_process].append(current_time + working_process[succeed_process][1])
    finished_program[succeed_process].append(finished_program[succeed_process][2]-working_process[succeed_process][2]) 
    finished_program[succeed_process].append(finished_program[succeed_process][3]-working_process[succeed_process][1]) 
        
    return finished_program,working_process
```
find the mean difference :
```
def avg_process(working_process,finished_program,current_time): #more CPU Utilization , avg Waiting time ,avg Turnaround
    avg_Waiting_time = 0
    avg_Turnaround = 0
    all_time_runprocess = 0
    CPU_Utilization = 0
    Throughput = 0
    for i in range (len(finished_program)):            
        avg_Waiting_time += finished_program[i][4]
        avg_Turnaround += finished_program[i][3] 

    for j in range (len(working_process)):            
        all_time_runprocess += working_process[j][1]
    
    Throughput =  max_data / all_time_runprocess   
    CPU_Utilization = (all_time_runprocess / current_time)*100 
    avg_Waiting_time = avg_Waiting_time / len(finished_program) 
    avg_Turnaround = avg_Turnaround / len(finished_program)   

    return avg_Waiting_time,avg_Turnaround,CPU_Utilization,Throughput
```
---
Ex. main2.py output :<br />
before read file "test2.csv":
| Process | Burst Time | Arrival Time |
|:---:|:----:|:---:|
| P1 | 10 | 20 |
| P2 | 5 | 15 |
| ... | ... | ... |

after:
| Process | start time | Exit time | Turnaround | Waiting time |
|:---:|:----:|:---:|:---:|:---:|
| P3 | 15 | 20 | 5 | 0 |
| P1 | 20 | 30 | 10 | 0 |
| ... | ... | ... | ... | ... |


<br />
all time = 452 s.<br />
Throughput = 13.15 s.<br />
Avg Waiting time = 44.75 s.<br />
Avg Turnaround = 57.9 s.<br />
CPU Utilization = 58.1858407079646 %<br />

---

 * Gantt chart <br />
 > support multi color in <= 50 process ,if process > 50 color = blue #array color = 50 colr <br />
 > if you don't want the color see file "cpu_scheduling2.py"  <br />
  <br />
Code show gantt chart "cpu_scheduling2.py" (no multi color) :

```
name_pro = []
num_y =[]

fig, gnt = plt.subplots()
len_maxp = len(finished_program)*5

gnt.set_xlabel('seconds ')
gnt.set_ylabel('Processor')
gnt.set_ylim(0, len_maxp)
gnt.set_xlim(0, current_time)
name_pro.append([])
num_y.append([])
yx = 2.5
for i in range (len(finished_program)):
    name_pro[0].append(finished_program[i][0])
for i in range (len(finished_program)):
    num_y[0].append(yx)
    yx += 5

gnt.set_yticks(num_y[0])
gnt.set_yticklabels(name_pro[0])
gnt.grid(True)

add_y = 0
for i in range (len(finished_program)):
    gnt.broken_barh([(finished_program[i][1], working_process[i][1])],(add_y, 5))
    add_y += 5

plt.show()
```
* Ex gantt chart "cpu_scheduling.py" read file "test.csv" :
![image](https://user-images.githubusercontent.com/94011063/193577799-81e72507-4922-459a-a973-ae1ba1a94f33.png) 
* Ex. GUI  <br />
![image](https://user-images.githubusercontent.com/94011063/193579140-fd10fede-a0b6-420d-849d-b19b45ac54b5.png)
* cpu_scheduling.py read file .csv only<br />
<br />
<br />

---

# Then like preemptive Longest Job First?  <br />
that code will be left main funtion orly (haven't found Turnaround and Waiting time a process yet) :
```
while succeed_process < max_data:
    if outside_process != []:
        for inum in list(outside_process):              #check current time with Arrival Time
            if inum[2] <= current_time :
                interesting_process.append(inum)        # process outside cpu => process inside cpu
                outside_process.remove(inum)            # remove process outside cpu
                
    if len(interesting_process) >= 1:                   #check process inside cpu
        if len(interesting_process) > 1 :
            interesting_process.sort(key=lambda i:i[1])  

        for inum in list(interesting_process):             
            if inum[1] == 0 :
                interesting_process.remove(inum)  
                succeed_process += 1

        working_process.append(interesting_process.pop())

        if len(working_process) == 1:
            if finished_program == [] or working_process[0][0] != finished_program[-1][0]:
                round+=1
                finished_program.append([])
                finished_program[round].append(working_process[0][0]) 
                finished_program[round].append(current_time)
                finished_program[round].append(1)
                finished_program[round].append(current_time + 1) 
                working_process[0][1] -= 1
            else:
                finished_program[round][3] += 1 
                finished_program[round][2] += 1 
                working_process[0][1] -= 1
            current_time += 1

        if working_process[0][1] == 0:
                succeed_process += 1
                working_process.pop()
        else:
            interesting_process.append(working_process.pop())

    else: 
        current_time += 1
```
---
will get this data table file "test3.csv":
| Process | start time | round burst time | Exit time |
|:---:|:----:|:---:|:---:|
| P1  | 0 | 1 | 1 |
| P2 | 0 | 12 | 13 |
| ... | ... | ... | ... |
* Gantt chart  <br />

![image](https://user-images.githubusercontent.com/94011063/194728806-3285b7b8-d67c-480c-8860-ed3ebc389036.png)  <br />

---

# and last RR ( Round Robin ) <br />
same code to preemptive will be left main funtion orly (haven't found Turnaround and Waiting time a process yet) :
```
while succeed_process < max_data:
    if outside_process != []:
        for inum in list(outside_process):              #check current time with Arrival Time
            if inum[2] <= current_time :
                interesting_process.append(inum)        # process outside cpu => process inside cpu
                outside_process.remove(inum)            # remove process outside cpu
                
    if stay_process != []:
        for punm in list(stay_process):
            interesting_process.append(punm)
            stay_process.remove(punm)

    if len(interesting_process) >= 1:                   
        while interesting_process != []:
            working_process.append(interesting_process.pop(0))

        for i in range(len(working_process)):
            round += 1
            if working_process[i][1] >= rr :
                finished_program.append([])
                finished_program[round].append(working_process[i][0])
                finished_program[round].append(current_time)
                finished_program[round].append(rr)
                finished_program[round].append(current_time + rr)
                working_process[i][1] -= rr
                current_time += rr
            else: 
                finished_program.append([])
                finished_program[round].append( working_process[i][0])
                finished_program[round].append(current_time)
                finished_program[round].append( working_process[i][1])
                finished_program[round].append(current_time +  working_process[i][1])
                current_time += working_process[i][1]
                working_process[i][1] = 0

        for p in list(working_process):
            if p[1] == 0 :
                working_process.remove(p)
                succeed_process += 1
            else:
                stay_process.append(p)
                working_process.remove(p)

    elif interesting_process == [] and outside_process != [] and stay_process != []: 
        current_time += 1
```
---
and will get this data table file "test3.csv" and RR = 5:
| Process | start time | round burst time | Exit time |
|:---:|:----:|:---:|:---:|
| P1  | 0 | 5 | 5 |
| P2 | 5 | 5 | 10 |
| ... | ... | ... | ... |
* Gantt chart  <br />

![image](https://user-images.githubusercontent.com/94011063/194737666-a5a08722-bf7b-438d-a13a-7fc129bf18b8.png)  <br />

---
