class Schedule:
    def __init__(self , task_name , n ,arrival_time, quantum , burst_time):
        self.task_name = task_name          # List of the names given to all tasks.
        self.n = n                          # Number of tasks.
        self.arrival_time = arrival_time    # List of arrival time of every task.
        self.quantum = quantum              # Variable for the time quantum.
        self.burst_time = burst_time        # List of burst time of every task.
        self.total_waiting_time = 0         # Variable for the sum of waiting time of all the tasks.
        self.total_turn_around_time = 0     # Variable for the sum of response time(turn_around time) of all the tasks.
        self.waiting_time = [0]*self.n      # List of waiting time of every task.
        self.turn_around_time = [0]*self.n  # List of response time (actual time taken to excecute and end the task) of every task.
        self.remaining_burst_time = [0]*self.n  #List to check the remaining process time of every task.
    #-----
    def process(self):
        '''
        This function does the task scheduling based on Round Robin Algorithm.
        '''
        for i in range(self.n):
            self.remaining_burst_time[i] = self.burst_time[i]   #Initially, the remaining burst time will be the actual burst time as no task is scheduled.
        
        self.current_time = 0           #To start counting the time.
        
        while True:
            self.complete = True    #To check whether all the tasks are completed or not.
            for i in range(self.n):
                if (self.arrival_time[i] <= self.current_time):     #Did the task i arrive? If yes, proceed for scheduling.
                    if (self.remaining_burst_time[i] > 0):  #If task is still not completed...
                        self.complete = False
                        if (self.remaining_burst_time[i] > self.quantum):   #If the remaining burst time exceeds the quantum time...
                            self.current_time += self.quantum       #Schedule the task until quantum time expires. Eventually, increment the current time.
                            self.remaining_burst_time[i] -= self.quantum        #Update the remaining burst time.
                        else:                                           #If the remaining burst time is less than quantum time...
                            self.current_time += self.remaining_burst_time[i]   #Complete the task and update the current time.
                            self.waiting_time[i] = self.current_time - self.burst_time[i] - self.arrival_time[i]   #Calculate the waiting time.
                            self.remaining_burst_time[i] = 0            #Task is completed. Hence, remaining burst time = 0.
                            self.turn_around_time[i] = self.burst_time[i] + self.waiting_time[i]   #It is the response time.
                else:
                    continue                #If the task i did not arrive, check the next one.
            if (self.complete == True):         #If this is not True, it means some tasks are still remaininig.
                break
    
        
        for i in range(self.n):
            self.total_turn_around_time += self.turn_around_time[i]     #The response time of all the tasks.(To calculate the average).
            self.total_waiting_time += self.waiting_time[i]         #The waiting time of all the tasks.(To calculate the average).
    #-----
    def output(self):
        '''
        This function displays the schedule. It also gives the avg. waiting time and avg. response time.
        '''
        print('\nTask  \tArrival_Time  \tBurst_Time\tWaiting_Time\tTurn_Around_time\n')
        for i in range(self.n):             #Print the details.
            print(self.task_name[i],'\t',self.arrival_time[i],'\t\t',self.burst_time[i] ,'\t\t',self.waiting_time[i],'\t\t',self.turn_around_time[i],end = ' ')
            print()
        
        print("_____________________________________________________________")
        print('\nAverage Waiting time : ',self.total_waiting_time/self.n)           #Display the average waiting time.
        print('\nAverage Turn_Around time : ',self.total_turn_around_time/self.n)   #Display the average response time.
