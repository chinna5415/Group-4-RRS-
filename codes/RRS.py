from random import randint      #Used to randomly choose an integer in a given range.
from time import clock          #Used to calculate the Rum time of the program.

class Schedule:
    def __init__(self , task_name , n , quantum , burst_time):
        self.task_name = task_name          # Variable for giving name to a task.
        self.n = n                          # Number of tasks.
        self.quantum = quantum              # Variable for the time quantum.
        self.burst_time = burst_time        # List of burst time of every task.
        self.total_waiting_time = 0         # Variable for the sum of waiting time of all the tasks.
        self.total_turn_around_time = 0     # Variable for the sum of response time(turn_around time) of all the tasks.
        self.waiting_time = [0]*self.n      # List of waiting time of every task.
        self.turn_around_time = [0]*self.n  # List of response time of every task.
        self.remaining_burst_time = [0]*self.n  #List to check the remaining process time of every task.
    
    def process(self):
        '''
        This function does the task scheduling based on Round Robin Scheme.
        '''
        for i in range(self.n):
            self.remaining_burst_time[i] = self.burst_time[i]   #Initially, the remaining burst time will be the actual burst time as no task is scheduled.
        self.current_time = 0           #To start the time count.
        
        while True:
            self.complete = True    #To check whether all the tasks are completed or not.
            for i in range(self.n):
                if (self.remaining_burst_time[i] > 0):  #If task is still not completed...
                    self.complete = False
                    if (self.remaining_burst_time[i] > self.quantum):   #If the remaining burst time exceeds the quantum time...
                        self.current_time += self.quantum       #Schedule the task until quantum time expires. Eventually, increment the current time.
                        self.remaining_burst_time[i] -= self.quantum        #Update the remaining burst time.
                    else:                                           #If the remaining burst time is less than quantum time...
                        self.current_time += self.remaining_burst_time[i]   #Complete the task and update the current time.
                        self.waiting_time[i] = self.current_time - self.burst_time[i]   #Calculate the waiting time.
                        self.remaining_burst_time[i] = 0            #Task is completed. Hence, remaining burst time = 0.
            if (self.complete == True):         #If this is not True, it means some tasks are still remaininig.
                break
    
        for i in range(self.n):
            self.turn_around_time[i] = self.burst_time[i] + self.waiting_time[i]   #It is the response time (actual time taken to excecute and end the task).
        
        for i in range(self.n):
            self.total_turn_around_time += self.turn_around_time[i]     #The response time of all the tasks.(To calculate the average).
            self.total_waiting_time += self.waiting_time[i]         #The waiting time of all the tasks.(To calculate the average).
 
    def output(self):
        '''
        This function displays the schedule. It also gives the avg. waiting time and avg. response time.
        '''
        print('\nTask  \tBurst_Time\tWaiting_Time\tTurn_Around_time\n')
        for i in range(self.n):             #Print the details.
            print(self.task_name[i],'\t',self.burst_time[i] ,'\t\t',self.waiting_time[i],'\t\t',self.turn_around_time[i],end = ' ')
            print()
        print('\nAverage Waiting time : ',self.total_waiting_time/self.n)           #Display the average waiting time.
        print('\nAverage Turn_Around time : ',self.total_turn_around_time/self.n)   #Display the average response time.

def Run():
    print('\n________ROUND ROBIN SCHEDULING________')
    n=int(input("Enter the number of processes: "))
    
    print("\nDo you want to choose the time quantum or, should it be chosen randomly?")
    print("Press 'y' if you want to choose else, press 'n'")
    choose_quantum = input()
    if (choose_quantum == 'y'):
        quantum = int(input("\nEnter the time quantum: "))  #Input the time quantum.
    elif (choose_quantum == 'n'):
        quantum = randint(1,5)      #Time quantum is randomly chosen from the list [1,2,3,4,5].
    else:
        print("\nPlease enter either 'y' or 'n'")
    
    task_name = [chr(65+i) for i in range(n)]   #Each task is given a name alphabetically, in chronological order.
    
    print("\nDo you want to choose the burst time or, should it be chosen randomly?")
    print("Press 'y' if you want to choose else, press 'n'")
    choose_burst = input()
    burst_time=[]
    if (choose_burst == 'y'):
        for i in range(n):
            print("Enter the Burst time of task",task_name[i],": ",end="")
            k = int(input())        #Input the burst time every task...
            burst_time.append(k)    # and append it to the list.
    elif (choose_burst == 'n'):
        burst_time = [randint(10,20) for i in range(n)] #Burst time for every task is randomly chosen from the list [10,11,12,13,14,15,16,17,18,19,20].
    else:
        print("\nPlease enter either 'y' or 'n'")
    
    print('\nAssumptions:\n   1.All tasks arrive in the beginning.\n   2.Time quantum =',quantum,'.')   #Assumptions
    
    test = Schedule(task_name , n , quantum , burst_time)
    start_time = clock()    #Count the Run time of this code, starting from here.
    test.process()  #Function call to start scheduling.
    end_time = clock()      #Count the Run time of this code till here.
    test.output()   #Function call to display the schedule.
    
    print("..._________________________________________________")
    print("Run time of this code=",end_time - start_time,"seconds")     #Display Run time of the code.

Run()   #Run the code.
