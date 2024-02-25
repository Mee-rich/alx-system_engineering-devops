#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - creates an infinite while loop
 * Return: Always (0)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - program that creates 5 zombie processes
 * Return: Always (0)
 */
int main(void)
{
	int i;
	pid_t zombie_pid;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		
		if (zombie_pid == -1)
		{
			perror("Fork failed");
			exit(EXIT_FAILURE);
		}


		if (zombie_pid == 0)
		{
			/* Child process */
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0); /* Child exits immediately becoming a zombie */
		}
	}
	
	infinite_while();

	return (0);
}
