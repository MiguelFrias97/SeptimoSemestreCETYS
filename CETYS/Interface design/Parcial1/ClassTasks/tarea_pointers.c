#include <stdio.h>

int i;
int num1 = 4;
int num2 = 6;
int num3 = 9;
int num4 = 3;
int num5 = 7;

int *pointer1 = &num1;
int *pointer2 = &num2;
int *pointer3 = &num3;
int *pointer4 = &num4;
int *pointer5 = &num5;

int result;

int main() {
	int arreglo[5] = {4,6,9,3,7};
	int *pointer_arr = arreglo;

	for (i = 0; i < (sizeof(arreglo)/sizeof(arreglo[0])); i++) {
		result = result + *(pointer_arr + i);
	}

	printf("Resultado de suma: %d\n",result);
	return 0;
	}
