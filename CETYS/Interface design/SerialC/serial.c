#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <termios.h>

#include "serial.h"

int fd;
struct termios options;
char write_b;
char read_b;
int bytes_written = 0;
int bytes_read = 0;
char *element;
char read_array;
int i = 0;

char test;

int openPort(){
	fd = open("/dev/ttyS0", O_RDWR | O_NOCTTY);

	if (fd == -1)
		perror("open_port: Unable to open port");

	tcgetattr(fd, &options);

	cfsetispeed(&options, B9600);
	cfsetospeed(&options, B9600);

	options.c_cflag |= (CLOCAL | CREAD);
	options.c_cflag &= ~PARENB;
	options.c_cflag &= ~CSTOPB;
	options.c_cflag &= ~CSIZE;
	options.c_cflag |= CS8;

	tcsetattr(fd,TCSANOW, &options);
	tcflush(fd, TCIFLUSH);

	return fd;
	}

void sendByte(char bytes_written){
	write_b += write(fd, &bytes_written, sizeof(bytes_written));
	printf("\n Bytes written: %d \n",write_b);
	}

char readByte(char bytes_read){
	bytes_read += read(fd, &read_b, 8);
	printf("Bytes read: %d	Data: %c \n", bytes_read, read_b);
	return read_b;
	}

void closePort(){
	close(fd);
	}

void sendArray(char array[],int size){
	//printf("Entre a enviar un array \n");
	for (i = 0; i < size; i++){
		sendByte(array[i]);
		//printf("Estoy enviando el array %c \n  ", array[i]);
	}
}

void readArray(char read_array,int size){
		readByte(read_array);
	}

