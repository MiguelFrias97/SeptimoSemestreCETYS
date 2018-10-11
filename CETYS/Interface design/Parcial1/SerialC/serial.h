#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <termios.h>

int openPort();
void sendByte(char bytes_written);
char readByte(char bytes_read);
void closePort();
void sendArray(char array[],int size);
void readArray(char read_array, int size);

