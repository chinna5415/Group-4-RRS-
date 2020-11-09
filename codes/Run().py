from random import randint      #Used for randomly choosing an integer in a given range.
import Class_Schedule as S           #This class does the scheduling.

def Run():
    '''
    This function is used to input all the required data for Round Robin Scheduling.
    '''
    print('\n________ROUND ROBIN SCHEDULING________')
    n=int(input("Enter the number of tasks: "))
    
    task_name = [chr(65+i) for i in range(n)]     #Each task is given a name alphabetically, in chronological order.
    #-----
    print("\nDo you want to choose the arrival time, or should it be chosen randomly?")
    print("Press 'y' if you want to choose, else press 'n'")
    arrival_time = [0]                          #First task arrives at time = 0.
    choose_arrival = input()
    while True :
        if (choose_arrival == 'y'):
            print("The arrival time of A : 0")                  
            for i in range(1,n):
                print("Enter the arrival time of task",task_name[i],": ") 
                arrival_time.append(int(input()))            #Input the arrival time every task and append it to the list.
            break
        elif (choose_arrival == 'n'):
            for i in range(1,n):
                arrival_time.append(randint(arrival_time[i-1],i+10))    #Other tasks arrive (randomly) after their previous tasks have arrived.
            break    
        else:
            print('you have to choose [y/n]')
            choose_quantum = input()
    #-----
    print("\nDo you want to choose the time quantum, or should it be chosen randomly?")
    print("Press 'y' if you want to choose, else press 'n'")
    choose_quantum = input()
    while True:
        if (choose_quantum == 'y'):
            quantum = int(input("\nEnter the time quantum: "))      #Input the time quantum.
            break
        elif (choose_quantum == 'n'):
            quantum = randint(1,5)      #Time quantum is randomly chosen from the list [1,2,3,4,5].
            break
        else:
            print('you have to choose [y/n]')
            choose_quantum = input()
    #-----
    print("\nDo you want to choose the burst time, or should it be chosen randomly?")
    print("Press 'y' if you want to choose, else press 'n'")
    choose_burst = input()
    burst_time=[]                               #List of burst times of all tasks. 
    while True:
        if (choose_burst == 'y'):
            for i in range(n):
                print("Enter the Burst time of task",task_name[i],": ")
                burst_time.append(int(input()))         #Input the burst time every task and append it to the list.
            break
        elif (choose_burst == 'n'):
            burst_time = [randint(11,20) for i in range(n)] #Burst time for every task is randomly chosen from the list [10,11,12,13,14,15,16,17,18,19,20].
            break
        else:
            print('you have to choose [y/n]')
            choose_burst = input()
    
    print('\nTime quantum =',quantum,'.')   #Display the time quantum.
    #-----
    test = S.Schedule(task_name , n , arrival_time, quantum , burst_time)
    test.process()  #Function call to start scheduling.
    test.output()   #Function call to display the schedule.

if __name__ == '__main__':
    Run()

    
def check_temp_bust_time(temp_bust_time, length):
    if temp_bust_time.count(0) == length:
        return 0
    return 1

def check_gant_chart(gant_chart, process_name):
    if process_name in gant_chart:
        return 0
    return 1

def getProcess(ready_queue, time, process, arival_time, temp_bust_time):
    min_bust_time = 999
    idx = ''
    for i in ready_queue:
        if min_bust_time > temp_bust_time[process.index(i)]:
            min_bust_time, idx = temp_bust_time[process.index(i)], i

    time += min_bust_time
    ele = idx
    ready_queue.remove(idx)
    temp_bust_time[process.index(idx)] = 0
    return ele, time

process = []
arival_time = []
bust_time = []

with open('data.txt','r') as file:
    for line in file:
        line = line.split(',')
        process.append(line[0])
        arival_time.append(int(line[1]))
        bust_time.append(int(line[2]))

ready_queue = []
gant_chart = []
complete_time = {i:0 for i in process}
temp_bust_time = []+bust_time
time = 0

while check_temp_bust_time(temp_bust_time, len(process)):
    for i in range(len(process)):
        if arival_time[i] <= time and check_gant_chart(gant_chart, process[i]):
            ready_queue.append(process[i])
            
    while ready_queue != []:
        ele, time = getProcess(ready_queue, time, process, arival_time, temp_bust_time)
        gant_chart.append(ele)
        complete_time[ele] = time

turn_around_time = []
sum_tat = 0
sum_wt = 0
i = 0

for key, value in complete_time.items():
    turn_around_time.append((value - arival_time[i]))
    sum_tat += turn_around_time[-1]
    sum_wt += (turn_around_time[-1] - bust_time[i])
    i += 1

print('Order of execution')
print(*gant_chart)
length = len(process)

print('Avarage Turn around time : %.2f'%(sum_tat/length))
print('Avarage waiting time : %.2f'%(sum_wt/length))
