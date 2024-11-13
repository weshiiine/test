#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/msg.h>
#include <sys/ipc.h>
#include <sys/shm.h>

#define SHMKEY 75 // 定义共享区关键词

int shmid, i;
int *addr;

void CLIENT() {
    int i;
    // 获取共享内存
    shmid = shmget(SHMKEY, 1024, 0777); // 获取共享区，长度1024，关键词SHMKEY
    addr = (int *)shmat(shmid, 0, 0);   // 获取共享区地址

    if (addr == (void *)-1) {
        perror("shmat failed");
        exit(1);
    }

    for (i = 9; i >= 0; i--) { // 用 i 从 9 到 0 循环
        while (*addr != -1); // 等待服务器处理完数据
        printf("(client) sent %d\n", i); // 打印发送的数据
        *addr = i; // 把数据写入共享内存
    }
    exit(0);
}

void SERVER() {
    // 创建共享内存
    shmid = shmget(SHMKEY, 1024, 0777 | IPC_CREAT); // 创建共享区
    addr = (int *)shmat(shmid, 0, 0);   // 获取共享区地址

    if (addr == (void *)-1) {
        perror("shmat failed");
        exit(1);
    }

    do {
        *addr = -1; // 将共享内存设置为 -1，表示客户端可以写入数据
        while (*addr == -1); // 等待客户端写入数据
        printf("(server) received %d\n", *addr); // 打印收到的数据
    } while (*addr != 0); // 当接收到的数据为 0 时停止

    // 删除共享内存
    shmctl(shmid, IPC_RMID, 0);
    exit(0);
}

int main() {
    pid_t pid1, pid2;

    pid1 = fork();
    if (pid1 > 0) {
        // 父进程
        pid2 = fork();
        if (pid2 > 0) {
            // 父进程等待子进程退出
            waitpid(pid1, NULL, 0);
            waitpid(pid2, NULL, 0);
        } else {
            // 子进程2，CLIENT
            CLIENT();
        }
    } else {
        // 子进程1，SERVER
        SERVER();
    }

    return 0;
}

