#if no module named 'pandas' you scanf "pip install pandas" in terminal
import pandas as pd
import matplotlib.pyplot as plt


# read by default 1st sheet of an excel file

data = pd.read_csv (r'test2.csv')
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
round = -1




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
            


print("| Process | start time | Exit time ")
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