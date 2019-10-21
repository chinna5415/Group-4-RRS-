using namespace std;
#include <iostream>
#include <cstdlib>
#include <ctime>
int n; // Global value n

class Robin {
    public :
            int burst_time[10] , process[10] , quantum , turn_around_time = 0 , waiting_time = 0;
            int wt[10] , tat[10];
            void get_data();
            void waitingtime(int quantum , int burst_time[] , int process[] , int wt[]);
            void turnaroundtime(int burst_time[] , int process[] , int wt[] , int tat[]);
            void print() {
                 cout << "Processes "<< " Burst time " << " Waiting time " << " Turn around time\n";
                 for (int i=0; i<n; i++) {
                     waiting_time = waiting_time + wt[i];
                     turn_around_time = turn_around_time + tat[i];
                     cout << " " << char(65+i) << "\t\t" << burst_time[i] <<"\t " << wt[i] <<"\t\t " << tat[i] << endl;
                  }

                  cout << "Average waiting time = " << (float)waiting_time / (float)n;
                  cout << "\nAverage turn around time = " << (float)turn_around_time / (float)n;
            }
};

void Robin :: get_data() {
     int random;
     cout << "enter the quantum : "; // assign the CPU time
     cin >> quantum;

     for (int i = 0 ; i < n ; i++) {
        process[i] = i;
        random = rand() % 55; // rand() it produce random numbers up to 55
        burst_time[i] = random;
     }
}

void Robin :: waitingtime(int quantum , int burst_time[] , int process[] , int wt[]) {
     int rem_bursttime[n] , t = 0;
     for (int i = 0 ; i < n ; i++)
        rem_bursttime[i] = burst_time[i];

     while (1) {
           bool done = true;
           for (int i = 0 ; i < n; i++) {
               if (rem_bursttime[i] > 0) {
                   done = false;
                   if (rem_bursttime[i] > quantum) {
                      t += quantum;
                      rem_bursttime[i] -= quantum;
                   }  else {
                             t = t + rem_bursttime[i];
                             wt[i] = t - burst_time[i];
                             rem_bursttime[i] = 0;
                   }
               }
            }

        if (done == true)
          break;
    }
}

void Robin :: turnaroundtime(int burst_time[] , int process[] , int wt[] , int tat[]) {
     for (int i = 0 ; i < n ; i++)
        tat[i] = burst_time[i] + wt[i];
}

int main() {
    clock_t start , end_;
    cout << "enter the number of process : "; // Input for number of process you want
    cin >> n;
    Robin r; // r -> class object

    start = clock(); // clock starts
    r.get_data(); // input function
    r.waitingtime(r.quantum , r.burst_time , r.process , r.wt); // This function calculate the waiting time
    r.turnaroundtime(r.burst_time , r.process , r.wt , r.tat); // This function calculate the turn around time
    end_ = clock(); // clock ends

    r.print(); // This function print the output

    cout << "\ntime : " << (end_ - start);
}
