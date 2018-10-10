#include <stdio.h>

int main() {
	// int arreglo[4] = {1,2,3,4};
	//areglo[0] = 1;

	int arreglo[4];
	int i;

	/*for (i = 0; i < 4; i++){
		arreglo[i] = 2*i;
		printf("El valor del arreglo en la posicion %d es %d \n",i,arreglo[i]);
	}*/

	for (i = 0; i < 255; i++){
		printf("Valor: %d  Caracter: %c \n",i,i);
	}
}
