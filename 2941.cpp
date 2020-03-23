#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int main() {

	char input[100];
	scanf("%s", input);

	int count = 0;

	for (int i = 0; i < (int)strlen(input); i++) {
		//printf("i : %d ", i);
		if (input[i] == 'c' &&  input[i+1] == '=') {	//c=
			i++;
			count++;
		}
		else if (input[i] == 'c' &&  input[i + 1] == '-') {	//c-
			i++;
			count++;
		}
		else if (input[i] == 'd' && input[i+1] == '-') {	//d-
			i++;
			count++;
		}
		else if ((i>=1) && input[i-1] == 'd' && input[i] == 'z' && input[i + 1] == '=') {	//dz=
			i++;
		}
		else if (input[i] == 'l' && input[i+1] == 'j') { //lj
			count++;
			i++;
		}
		else if (input[i] == 'n' && input[i+1] == 'j') {	//nj
			i++;
			count++;
		}
		else if (input[i] == 's' && input[i+1] == '=') {	//s=
			count++;
			i++;
		}
		else if (input[i] == 'z' && input[i+1] == '=') { //z=
			i++;
			count++;
		}
		else
			count++;

		//printf("count : %d\n", count);
	}

	printf("%d\n", count);

	return 0;
}