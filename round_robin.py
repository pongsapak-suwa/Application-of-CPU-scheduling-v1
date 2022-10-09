#if no module named 'pandas' you scanf "pip install pandas" in terminal
import pandas as pd
import matplotlib.pyplot as plt


# read by default 1st sheet of an excel file

data = pd.read_csv (r'test3.csv')
df = pd.DataFrame(data, columns= ['Process','Burst Time','Arrival Time']).to_numpy()

max_data = len(df)          #Maximum of data
max_process = df
outside_process = []            #process outside cpu
for inum in list(max_process):          #Enter an array 
    outside_process.append(inum)
outside_process.sort(key=lambda i:i[2])     #fix bug by sort Arrival Time

succeed_process = int(0)        #current succeed process
current_time = int(0)           #start current time
interesting_process = []        #process outside cpu
finished_program = []           #process at finished data in [[Process],[start time],[end time],[Turnaround],[Waiting time]]
working_process = []            #same process at finished but data like df [[Process],[Burst Time],[Arrival Time]]
stay_process = []
round = -1
rr = 5



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
            


print("| Process | start time | round burst time | Exit time ")
print("===============================================================")
for i in range (len(finished_program)):
    print(finished_program[i][0],"\t|\t",finished_program[i][1],"\t|\t",finished_program[i][2],"\t|\t",finished_program[i][3],"\t|\t")
    print("----------------------------------------------------------------")

name_pro = []
num_y =[]

fig, gnt = plt.subplots()
len_maxp = len(finished_program)*5
#support color in <= 50 process ,if process > 50 color = blue

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
    gnt.broken_barh([(finished_program[i][1], finished_program[i][2])],(add_y, 5))
    add_y += 5

plt.show()