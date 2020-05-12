#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "func_memory.h"

//#pragma warning(disable:4996)

void calc_towns_matrix(double** towns_matrix, int townsCount) {
	//double** matrix = NULL;
	//int count = atoi(args[1]);
	srand(time(NULL));
	initialize_matrix(&towns_matrix, townsCount);

	for (int i = 0; i < townsCount; i++) {
		for (int j = i; j < townsCount; j++) {
			if (i != j) {
				towns_matrix[i][j] = (double)(rand() % 7000000) / 700;
				towns_matrix[j][i] = towns_matrix[i][j];
			}
			else {
				towns_matrix[i][j] = 0.0;
			}
		}
	}

	//FILE* file = fopen(args[2], "w");
	//fprintf(file, "%d\n", count);
	//for (int i = 0; i < count; i++) {
	//	for (int j = 0; j < count; j++)
	//		fprintf(file, "%lf ", matrix[i][j]);
	//	fprintf(file, "\n");
	//}
	//fclose(file);
	//free(matrix);
	//return 0;
};
