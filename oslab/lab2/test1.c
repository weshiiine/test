#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>  // For wait()
#include <unistd.h>
#include <stdlib.h>  // For exit()

int main() 
{
    pid_t pid;
    char *path = "/bin/ps"; 
    char *argv[5] = {"ps", "-a", "-x", NULL}; 

    printf("Run ps with execve by child process:\n");

    if ((pid = fork()) < 0) {
        printf("fork error!\n");
        exit(1);
    }
    else if (pid == 0) {
        if (execve(path, argv, NULL) < 0) {
            printf("execve error!\n");
            exit(1);
        }
        // This line will never be reached if execve is successful.
        printf("child is ok!\n");
        exit(0);
    }
    
    // Parent process waits for the child to finish
    wait(NULL); 
    printf("It is ok!\n");

    return 0;
}

