#include <stdlib.h>


#define n 512

double a[n][n];
double b[n][n];
double c[n][n];

int main()
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			a[i][j] = (double)rand() / 1000;
			b[i][j] = (double)rand() / 1000;
			c[i][j] = 0;
		}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			for (int k = 0; k < n; k++)
				c[i][j] += a[i][k]*b[k][j];

	return 0;
}
