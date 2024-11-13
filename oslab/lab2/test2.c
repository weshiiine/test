#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>

void waiting();
void stop();
void alarming();

int wait_mark;

int main() {
    int p1, p2;

    if ((p1 = fork())) { // 创建子进程 p1
        if ((p2 = fork())) { // 创建子进程 p2
            wait_mark = 1;
            signal(SIGINT, stop);    // 接收到 ^C 信号时，调用 stop
            signal(SIGALRM, alarming); // 接收到 SIGALRM 时，调用 alarming
            waiting(); // 父进程等待

            // 向 p1 发送 SIGTERM（软中断）
            kill(p1, SIGTERM); 

            // 向 p2 发送 SIGTERM（软中断）
            kill(p2, SIGTERM);

            // 等待两个子进程退出
            wait(0);
            wait(0);

            printf("Parent process is killed!\n");
            exit(0);
        } else {
            wait_mark = 1;
            signal(SIGTERM, stop); // 接收到 SIGTERM 信号时，调用 stop
            signal(SIGINT, SIG_IGN);  // 忽略 SIGINT 信号
            while (wait_mark != 0);
            
            printf("Child process2 is killed by parent!\n");
            exit(0);
        }
    } else {
        wait_mark = 1;
        signal(SIGTERM, stop); // 接收到 SIGTERM 信号时，调用 stop
        signal(SIGINT, SIG_IGN); // 忽略 SIGINT 信号
        while (wait_mark != 0);

        printf("Child process1 is killed by parent!\n");
        exit(0);
    }

    return 0;
}

void waiting() {
    sleep(5);
    if (wait_mark != 0)
        kill(getpid(), SIGALRM);  // 发送 SIGALRM 信号给父进程
}

void alarming() {
    wait_mark = 0;  // 父进程接收到 SIGALRM，更新 wait_mark
}

void stop() {
    wait_mark = 0;  // 子进程接收到 SIGTERM，更新 wait_mark
}

