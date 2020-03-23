#include <cstdio>
#include <cmath>
#define PI 3.1415926535897932
using namespace std;

int main() {

	int r;
	scanf("%d", &r);

	printf("%.5f\n", PI*pow(r,2));
	printf("%.5f\n", 2*pow(r,2));


	return 0;
}