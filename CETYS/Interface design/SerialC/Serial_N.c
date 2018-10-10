#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <termios.h>

void main(){
	int fd;
	struct termios options;
	char write_buffer = 'A';
	char read_buffer;
	int bytes_written = 0;
	int bytes_read = 0;
	int i = 0;

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

	bytes_written = write(fd, &write_buffer, sizeof(write_buffer));
	printf("\n Bytes written: %d \n",bytes_written);

	bytes_read = read(fd, &read_buffer, 8);
	printf("Bytes read: %d	Data: %c \n", bytes_read, read_buffer);

	close(fd);
}
