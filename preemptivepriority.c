//Write a program to implement preemptive priority based scheduling algorithm.

#include <stdio.h>

struct Process {
    int id, bt, at, pr, rt;
};

int main() {
    int n, time = 0, completed = 0, shortest = -1;
    float total_wt = 0, total_tat = 0;
    int finish_time, min_priority = 999;

    printf("Enter the number of processes: ");
    scanf("%d", &n);

    struct Process p[n];

    for (int i = 0; i < n; i++) {
        printf("Enter Arrival Time, Burst Time and Priority for P[%d]:\n", i + 1);
        p[i].id = i + 1;
        scanf("%d %d %d", &p[i].at, &p[i].bt, &p[i].pr);
        p[i].rt = p[i].bt;
    }

    printf("\nProcess\tTurnaround Time\tWaiting Time\n");

    while (completed != n) {
        shortest = -1;
        min_priority = 999;

        for (int i = 0; i < n; i++) {
            if (p[i].at <= time && p[i].rt > 0 && p[i].pr < min_priority) {
                min_priority = p[i].pr;
                shortest = i;
            }
        }

        if (shortest == -1) {
            time++;
            continue;
        }

        p[shortest].rt--;

        if (p[shortest].rt == 0) {
            completed++;
            finish_time = time + 1;
            int tat = finish_time - p[shortest].at;
            int wt = tat - p[shortest].bt;
            total_tat += tat;
            total_wt += wt;
            printf("P[%d]\t%d\t\t%d\n", p[shortest].id, tat, wt);
        }

        time++;
    }

    printf("\nAverage Waiting Time = %.2f\n", total_wt / n);
    printf("Average Turnaround Time = %.2f\n", total_tat / n);

    return 0;
}
