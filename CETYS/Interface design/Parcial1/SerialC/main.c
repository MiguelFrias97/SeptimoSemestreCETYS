#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <termios.h>

#include "serial.h"

char write_buffer = 'Z';
char write_buffer2 = 'A';
char read_buffer;
char read_array;
char array[6] = {'M','I','G','U','E','L'};
int lock = 0;
int array_size = 6;

void main(){
	lock = openPort();
	if (lock >= 1){
	//sendByte(write_buffer);
	//sendByte(write_buffer2);
	//readByte(read_buffer);
	sendArray(array,array_size);
	readArray(read_array,array_size);
	closePort();
	}
}
