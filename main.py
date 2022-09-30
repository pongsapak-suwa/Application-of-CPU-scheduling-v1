#if no module named 'pandas' you scanf "pip install pandas" in terminal
import pandas as pd

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


def longest_burst_time(interesting_process):            #look for Longest process
    if len(interesting_process) > 1 :
        interesting_process.sort(key=lambda i:i[1])     #sort process if process > 1
    
    working_process.append(interesting_process.pop())      #pop process very long at process working

    return working_process

def process_suv(succeed_process,current_time,working_process): #more finished program
    finished_program.append([])
    finished_program[succeed_process].append(working_process[succeed_process][0]) #name process
    finished_program[succeed_process].append(current_time)                          #start time = current time
    finished_program[succeed_process].append(current_time + working_process[succeed_process][1]) #Exit time = current time + Burst Time
    finished_program[succeed_process].append(finished_program[succeed_process][2]-working_process[succeed_process][2])  #Turnaround = Exit time - Arrival Time
    finished_program[succeed_process].append(finished_program[succeed_process][3]-working_process[succeed_process][1])  #Waiting time = Turnaround - Burst Time
        
    return finished_program,working_process


def avg_process(working_process,finished_program,current_time): #more CPU Utilization , avg Waiting time ,avg Turnaround
    avg_Waiting_time = 0
    avg_Turnaround = 0
    all_time_runprocess = 0
    CPU_Utilization = 0
    Throughput = 0
    for i in range (len(finished_program)):             #all Turnaround and waiting time
        avg_Waiting_time += finished_program[i][4]
        avg_Turnaround += finished_program[i][3] 

    for j in range (len(working_process)):              #all time to run process
        all_time_runprocess += working_process[j][1]
    
    Throughput =  all_time_runprocess / max_data                #Throughput = all time to run process / all process
    CPU_Utilization = (all_time_runprocess / current_time)*100  #CPU Utilization <= 100%
    avg_Waiting_time = avg_Waiting_time / len(finished_program) #avg Waiting time = all waiting time / all process
    avg_Turnaround = avg_Turnaround / len(finished_program)     #avg Turnaround = all Turnaround / all process

    return avg_Waiting_time,avg_Turnaround,CPU_Utilization,Throughput


while(succeed_process < max_data):
    if outside_process != []:
        for inum in list(outside_process):              #check current time with Arrival Time
            if inum[2] <= current_time :
                interesting_process.append(inum)        # process outside cpu => process inside cpu
                outside_process.remove(inum)            # remove process outside cpu
    if len(interesting_process) >= 1:                   #check process inside cpu
        longest_burst_time(interesting_process)
        process_suv(succeed_process,current_time,working_process)
            
        current_time += working_process[succeed_process][1]
        succeed_process += 1

    elif (interesting_process == [])and (outside_process != []): # no process inside cpu and have process outside cpu spare time +1
        current_time += 1

avg_Waiting_time,avg_Turnaround,CPU_Utilization,Throughput = avg_process(working_process,finished_program,current_time) 

print("Process |","start time \t|","Exit time \t|","Turnaround    |","Waiting time")
print("========================================================================")
for i in range (len(finished_program)):
    print(finished_program[i][0],"\t|\t",finished_program[i][1],"\t|\t",finished_program[i][2],"\t|\t",finished_program[i][3],"\t|\t",finished_program[i][4],)
    print("----------------------------------------------------------------------")
print("all time =",current_time,"s.")
print("Throughput =",Throughput,"s.")
print("Avg Waiting time =",avg_Waiting_time,"s.")
print("Avg Turnaround =",avg_Turnaround,"s.")
print("CPU Utilization =",CPU_Utilization ,"%")
