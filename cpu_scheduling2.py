#Install "pip install pandas" in terminal
import pandas as pd
#Install Tkinter "pip install tk" in terminal
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
#Install matplotlib "pip install matplotlib" in terminal
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry("1000x540")

def search_file():
        fileopen = askopenfile()
        lable_search = Label(text = fileopen ).pack()
        

root.title('Application of CPU scheduling - Non-preemptive Longest Job First')

head_text = tk.Label(root,text="Application of CPU scheduling - Non-preemptive Longest Job First")
head_text.grid(row=0,column=0)
my_font1=('times', 12, 'bold')
l1 = tk.Label(root,text='Read File & create DataFrame',width=30 )
l1.grid(row=1,column=0,sticky="E")
search_buttom = tk.Button(root, text='Browse File', width=15,command = lambda:upload_file())
search_buttom.grid(row=1,column=0,sticky="W")
l2 = tk.Label(root,text='before scheduling :',width=30)
l2.grid(row=1,column=1,sticky="W")
t1=tk.Text(root,width=45,height=20 )
t1.grid(row=2,column=0,padx=5,sticky="W")
l2 = tk.Label(root,text='after scheduling :',width=30 )
l2.grid(row=1,column=1,sticky="W")
t2=tk.Text(root,width=75,height=20 )
t2.grid(row=2,column=1,padx=5,sticky="W")



text_alltime = tk.Label(root,text=" all time = ",width=30 )
text_alltime.grid(row=10,column=0,sticky="W")      
l_alltime = tk.Label(root,text='0'+ 's.',width=30 )
l_alltime.grid(row=10,column=0,sticky="E")
text_Throughput = tk.Label(root,text=" Throughput = ",width=30 )
text_Throughput.grid(row=11,column=0,sticky="W") 
l_Throughput = tk.Label(root,text='0'+ 'p/s.',width=30 )
l_Throughput.grid(row=11,column=0,sticky="E")
text_avgwait = tk.Label(root,text="Avg Waiting time = ",width=30 )
text_avgwait.grid(row=12,column=0,sticky="W") 
l_avgwait = tk.Label(root,text='0'+'s/p.',width=30 )
l_avgwait.grid(row=12,column=0,sticky="E")
text_avgturn = tk.Label(root,text="Avg Turnaround = ",width=30 )
text_avgturn.grid(row=13,column=0,sticky="W") 
l_avgturn = tk.Label(root,text='0' +'s/p.',width=30 )
l_avgturn.grid(row=13,column=0,sticky="E")
text_Utilization = tk.Label(root,text="CPU Utilization = ",width=30 )
text_Utilization.grid(row=14,column=0,sticky="W") 
l_Utilization = tk.Label(root,text='0' +'%')
l_Utilization.grid(row=14,column=0,sticky="E")


def upload_file():
    run_buttom = tk.Button(root, text='run', width=15,command = lambda:[scheduling_file(),avg_output()])
    run_buttom.grid(row=1,column=1,sticky="E")

         
    t1.delete(1.0,END)
    f_types = [('CSV files',"*.csv"),('All',"*.*")]
    file = filedialog.askopenfilename(filetypes=f_types)
    l1.config(text=file) # display the path 
    data = pd.read_csv(file) # create DataFrame
    df = pd.DataFrame(data, columns= ['Process','Burst Time','Arrival Time']).to_numpy()
    max_data = len(df)          #Maximum of data
    max_process = df
    outside_process = []            #process outside cpu
    for inum in list(max_process):          #Enter an array
        outside_process.append(inum)
    str1 = "Process |  Burst Time   |  Arrival Time"
    t1.insert(tk.END, str1)
    str1 = "\n"
    t1.insert(tk.END, str1)
    for i in range(len(outside_process)):
        str1 = outside_process[i][0]
        t1.insert(tk.END, str1)
        str1 = "\t|\t"
        t1.insert(tk.END, str1)
        str1 = outside_process[i][1]
        t1.insert(tk.END, str1)
        str1 = "\t|\t"
        t1.insert(tk.END, str1)
        str1 = outside_process[i][2]
        t1.insert(tk.END, str1)
        str1 = "\n"
        t1.insert(tk.END, str1)

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
        
        Throughput =  max_data /  all_time_runprocess             #Throughput = all time to run process / all process
        CPU_Utilization = (all_time_runprocess / current_time)*100  #CPU Utilization <= 100%
        avg_Waiting_time = avg_Waiting_time / max_data #avg Waiting time = all waiting time / all process
        avg_Turnaround = avg_Turnaround / max_data       #avg Turnaround = all Turnaround / all process

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
    avg_Waiting_time,avg_Turnaround_time,CPU_Utilization,Throughput = avg_process(working_process,finished_program,current_time)


    def scheduling_file():
        '''
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
        '''
        t2.delete(1.0,END)
        str2 = "Process |  Start time   |   Exit time   |   Turnaround  |  Waiting time"
        t2.insert(tk.END, str2)
        str2 = "\n"
        t2.insert(tk.END, str2)

        for i in range (len(finished_program)):
            str2 = finished_program[i][0]
            t2.insert(tk.END, str2)
            str2 = "\t|\t"
            t2.insert(tk.END, str2)
            str2 = finished_program[i][1]
            t2.insert(tk.END, str2)
            str2 = "\t|\t"
            t2.insert(tk.END, str2)
            str2 = finished_program[i][2]
            t2.insert(tk.END, str2)
            str2 = "\t|\t"
            t2.insert(tk.END, str2)
            str2 = finished_program[i][3]
            t2.insert(tk.END, str2)
            str2 = "\t|\t"
            t2.insert(tk.END, str2)
            str2 = finished_program[i][4]
            t2.insert(tk.END, str2)
            str2 = "\n"
            t2.insert(tk.END, str2)

            gantt_buttom = tk.Button(root, text='see gantt chart', width=25,command = lambda:gantt__output())
            gantt_buttom.grid(row=15,column=1,sticky="E")



    def avg_output():
        l_alltime.config(text=str(current_time) + '\ts.')
        l_Throughput.config(text=str(Throughput) +'\tp/s.')
        l_avgwait.config(text=str(avg_Waiting_time) +'\ts/p.')
        l_avgturn.config(text=str(avg_Turnaround_time) +'\ts/p.')
        l_Utilization.config(text=str(CPU_Utilization) +'\t%')

    def gantt__output():
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
root.mainloop()
