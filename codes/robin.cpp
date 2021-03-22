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
     int random ;
     char choose_quantum , choose_burst_time , choose_arrival_time;
     cout << "\nDo you want to choose the time quantum(--> y), or choose randomly? (--> n)";
     cin >> choose_quantum;
     while (true) {
        if (choose_quantum == 'y') {
            cout << "\nEnter the time quantum: ";
            cin >> quantum;
            break;
        }
        if (choose_quantum == 'n') {
            quantum = rand() % 5;
            break;
        } else {
            cout << "you have to choose [y/n]";
            cin >> choose_quantum;}
     }

     cout << "\nDo you want to choose the arrival time (--> y) , or choose randomly? (--> n)\n ";
     cin >>choose_arrival_time;
     while (true) {
        if (choose_arrival_time == 'y') {
            arrival_time[0] = 0;
            for (int i = 1 ; i < n ; i++) {
                cout << "Enter the arrival time of " << char(65+i) << " : ";
                cin >> arrival_time[i];
            }
            break;
        }
        if (choose_arrival_time == 'n') {
            for (int i = 0 ; i < n ; i++) {
                random = rand() % 10;
                arrival_time[i] = random;
            }
            break;
        } else {
            cout << 'you have to choose [y/n]';
            cin >> choose_arrival_time; }
     }
     cout << "\nDo you want to choose the burst time(---> 'y'), or should it be chosen randomly?(--> n)\n";
     cin >> choose_burst_time;
     while (true) {
        if (choose_burst_time == 'y') {
            for (int i = 0 ; i < n ; i++) {
                cout << "enter the process " << char(65+i) << "Burst time : ";
                cin >> burst_time[i];
            }
            break;
        }
        if (choose_burst_time == 'n') {
            for (int i = 0 ; i < n ; i++) {
                random = rand() % 55;
                burst_time[i] = random;
            }
            break;
        } else {
            cout << 'you have to choose [y/n]';
            cin >> choose_arrival_time;}
     }

     cout << "\nTime quantum : " << quantum << "\n\n";
}

void Robin :: waitingtime(int quantum , int burst_time[] , int process[] , int wt[]) {
     int rem_bursttime[n] , t = 0;
     for (int i = 0 ; i < n ; i++)
        rem_bursttime[i] = burst_time[i];

     while (1) {
           bool done = true;
           for (int i = 0 ; i < n; i++) {
               if (arrival_time[i] <= t) {
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
               } else { continue ;}
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


#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

class SensorData {
/*
    This class stores the data about the sensors.
    It also has methods to raise or stop the fire alam.
*/
public:
    int SensorId;      // Stores the ID of the sensor.
    int TrackNumber, SectorNumber;   // Stores the coordinates of the sensor.
    bool fire_alarm;        // Flag variable. Set to 'true' when fire is detected.
    
    void set_Data(int , int , int);     // Assigns the data to the sensor.
    void Flag();        // Raises the alarm.
    void unFlag();      // Stops the alarm.
};

void SensorData::set_Data(int id, int t, int s) {
    this -> SensorId = id;
    this -> TrackNumber = t;
    this -> SectorNumber = s;
}

void SensorData::Flag() {
    this -> fire_alarm = true;
}

void SensorData::unFlag() {
    this -> fire_alarm = false;
}

static int Tracks, Sectors, SensorPerCell, SensorCount = 0;

void PlaceSensors(SensorData* ptr);
void ShowDatabase(SensorData* ptr);
void LocateSensor(SensorData* ptr);

int main() {
    char check;

    cout << "\nEnter the number of tracks in the field: ";
    cin >> Tracks;      // Input the number of tracks.
    
    cout << "Enter the number of sectors in the field: ";
    cin >> Sectors;     // Input the number of sectors.
    
    cout << "Enter the number of sensors per cell: ";
    cin >> SensorPerCell;     // Input the number of sensors per cell.
    
    // Create an array of objects of class SensorData.
    // Each object corresponds to a sensor placed in the field.
    // Total number of sensors in the field = tracks * sectors * sensor_per_cell
    SensorData sensor[Tracks * Sectors * SensorPerCell];
    SensorData* ptr = sensor;   // A pointer to reference the objects from differnet functions.
    
    PlaceSensors(ptr);  // Call the function to place the sensors in the field.
    
    cout << "\n\n--Press '1' to check for fire\n\t'2' to view database\n\t'0' to exit\n";
    
    // Based on the choice of the user, check for fire or exit.
    while(1) {
        cin >> check;

        if (check == '1') {
            // Randomly decide whether to raise the fire alarm or not.
            srand(time(NULL));
            int fire = rand() % 2;
            
            if (fire == 1) {
                // If decided to raise the fire alarm, randomly select
                // a sensor and set the flag to 1.
                srand((unsigned) time(0));
                sensor[(rand() % sensor_count) + 1].Flag();
    
                // Call the function to check which sensor has raised the alarm.
                LocateSensor(ptr);
            }
            else cout << "\t--- No Fire detected ---\n";
        }
        else if(check == '2') ShowDatabase(ptr); // Function to view the database.
        
        else if (check == '0') break;
    }
    return 0;
}

void PlaceSensors(SensorData* ptr) {
    /* This function will use the inputs from user to determine the
       field dimensions and place the sensors in the field, simultaneously
       adding the data to the database (objects)
    */
    for (int i=1; i<=Tracks; i++)
        for (int j=1; j<=Sectors; j++)
            for (int k=1; k<=SensorPerCell; k++) {
                ptr[SensorCount].set_Data(sensor_count+1, i, j);
                ptr[SensorCount].unFlag();
            
                SensorCount++;
            }
    cout << "\n" << SensorCount << " sensors are placed in the field.";
    
    ShowDatabase(ptr);
}

void LocateSensor(SensorData* ptr) {
    /* This function will locate the sensor which
       raised the fire alarm. After retrieving the sensor data,
       it will output the details. Then, it will stop the alarm.
    */
    for (int k=0; k<SensorCount; k++)
        if (ptr[k].fire_alarm) {
            cout << "\t--- FIRE ---\n\t Sensor ID : " << ptr[k].SensorId << "\n\t Track Number : " << ptr[k].TrackNumber << "\n\t Sector Number : " << ptr[k].SectorNumber << "\n\n";
        
            ptr[k].unFlag();
    }
}

void ShowDatabase(SensorData* ptr) {
    /* This function will display the complete
       data available about the sensors
    */
    cout << "\n  Sensor ID\tTrack Number\tSector Number";
    cout << "\n ---------------------------------------------";

    for(int k=0; k<SensorCount; k++)
        cout << "\n\t" << ptr[k].SensorId << "\t\t" << ptr[k].TrackNumber << "\t\t " << ptr[k].SectorNumber;
    cout << "\n ---------------------------------------------\n";
}
