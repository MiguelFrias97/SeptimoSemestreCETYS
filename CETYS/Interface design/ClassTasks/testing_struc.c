#include <stdio.h>

struct Person{
	char nombre[10];
	int edad;
};

int main(){
	struct Person p1;
	int i,length;

	p1.nombre[0] = 'A';
	p1.nombre[1] = 'B';
	p1.nombre[2] = 'A';
	p1.nombre[4] = '\0';
	p1.edad = 10;

	length = sizeof(p1.nombre)/sizeof(p1.nombre[0]);
	for (i = 0; i < length; i++){
		printf("%c",p1.nombre[i]);
	}

	printf("\n");
	printf("Edad: %d \n",p1.edad);

	return 0;
}
