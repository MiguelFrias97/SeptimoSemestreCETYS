#include <stdio.h>

int main() {
	int x;
	int *pointer; //pointer

	x = 5;
	pointer = &x; //con esto obtengo la direccion de X y la guardo en el
			//puntero "pointer"
	printf("Valor x con puntero: %d, la direccion es: %p \n",*pointer,pointer);

	*pointer = 7;

	printf("El numero valor de x: %d \n", *pointer);

	return 0;
}
