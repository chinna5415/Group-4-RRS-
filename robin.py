class robin():
    def __init__(self , n , b , q):
        self.n = n
        self.b = b
        self.q = q
        self.total_wt = 0
        self.total_tat = 0
        self.rbt = [0]*len(self.n)
        self.time = [0]*len(self.n)
        self.wt = [0]*len(self.n)
    def find_scheduling_time(self):
        self.t = 0
        for i in range(len(self.n)):
            self.rbt[i] = self.b[i]
        while 1 :
            self.done = True 
            for i in range(len(self.n)):
                if (self.rbt[i] > 0):
                    self.done = False
                    if (self.rbt[i] > self.q):
                       self.t += self.q
                       self.rbt[i] -= self.q
                    else :
                        self.t += self.rbt[i]
                        self.wt[i] = self.t - self.b[i]
                        self.rbt[i] = 0  
            if self.done == True :            
                self.turn_Around_time()
                break
            
    def turn_Around_time(self):
        for i in range(len(self.n)):
            self.time[i] = self.wt[i] + self.b[i]
        self.print_details()
        
    def print_details(self):
        print('Processes\tBrust_time\tWaiting_time\tTurn_Around_Time')
        for i in range(len(self.n)):
            self.total_wt += self.wt[i]
            self.total_tat += self.time[i]
            print(chr(65+i),'\t\t',self.b[i],'\t\t',self.wt[i],'\t\t',self.time[i])
        print('\nAverage waiting time : ',self.total_wt/len(self.n))
        print('\nAverage turn around time : ',self.total_tat / len(self.n))
                        

num_of_process = [1,2,3,4]
burst_time = [15,20,10,5]
quntum = 3

r = robin(num_of_process , burst_time , quntum)
r.find_scheduling_time()