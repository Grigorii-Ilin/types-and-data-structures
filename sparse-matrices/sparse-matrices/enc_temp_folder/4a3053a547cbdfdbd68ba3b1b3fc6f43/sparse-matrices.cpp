#include <iostream>
#include <ctime>
#include <vector>
#include <Windows.h>
#include <locale.h>
#include "sm.h"
using namespace std;

SparseMatrixClass Multiplication(SparseMatrixClass&, SparseMatrixClass&);
SparseMatrixClass Addition(SparseMatrixClass&, SparseMatrixClass&);
void Menu(void);
void Calculation(int);
void Output(SparseMatrixClass&, SparseMatrixClass&, SparseMatrixClass&);


void SetRussian() {
	const UINT CODE_PAGE_ID = 1251;
	SetConsoleCP(CODE_PAGE_ID);
	SetConsoleOutputCP(CODE_PAGE_ID);
	setlocale(LC_ALL, "rus");
}

SparseMatrixClass Multiplication(SparseMatrixClass& matrix1, SparseMatrixClass& matrix2) {

	int row = matrix1.Rows();
	int column = matrix2.Columns();

	if (matrix1.Columns() != matrix2.Rows()) {
		cout << "Неверное значение строк и столбцов матриц!" << endl;
		system("pause");
		exit(-1);
	}
	SparseMatrixClass Result(row, column);

	for (int r = 0; r < matrix1.JR.size(); r++) {
		for (int c = 0; c < matrix2.JC.size(); c++) {

			vector<int>columns;
			vector<int> values1;

			vector<int> rows;
			vector<int>values2;

			if (matrix1.JR[r] != -1) {
				int next = matrix1.JR[r];
				do {
					int col = -1;
					for (int i = 0; i < matrix1.JC.size(); i++)
						if (matrix1.JC[i] == next)
							col = i;
					if (col == -1) {
						int nextCol = matrix1.NC[next];
						while (nextCol != next) {
							for (int j = 0; j < matrix1.JC.size(); j++)
								if (nextCol == matrix1.JC[j])
									col = j;
							nextCol = matrix1.NC[nextCol];
						}
					}
					values1.push_back(matrix1.AN[next]);
					columns.push_back(col);
					next = matrix1.NR[next];
				} while (next != matrix1.JR[r]);
			}

			int val2 = 0;
			int resultVal = 0;
			if (matrix2.JC[c] != -1) {
				int next2 = matrix2.JC[c];
				do {
					int row2 = -1;
					for (int i = 0; i < matrix2.JR.size(); i++)
						if (matrix2.JR[i] == next2) {
							row2 = i;
						}
					if (row2 == -1) {
						int nextRow = matrix2.NR[next2];
						while (nextRow != next2) {
							for (int j = 0; j < matrix2.JR.size(); j++) {
								if (nextRow == matrix2.JR[j]) {
									row2 = j; val2 = matrix2.AN[next2];
								}
							}
							nextRow = matrix2.NR[nextRow];
						}
					}
					values2.push_back(matrix2.AN[next2]);
					rows.push_back(row2);
					next2 = matrix2.NC[next2];
				} while (next2 != matrix2.JC[c]);

				for (int i1 = 0; i1 < columns.size(); i1++) {
					for (int i2 = 0; i2 < rows.size(); i2++) {
						if (columns[i1] == rows[i2]) {
							resultVal += values1[i1] * values2[i2];
						}
					}
				}

				Result.Add(resultVal, r, c);

			}
		}
	}
	Result.Boxing();
	Result.Reset();
	return Result;
}


SparseMatrixClass Addition(SparseMatrixClass& matrix1, SparseMatrixClass& matrix2) {
	int rows1 = matrix1.Rows();
	int rows2 = matrix2.Rows();
	int columns1 = matrix1.Columns();
	int columns2 = matrix2.Columns();

	if (rows1 != rows2 && columns1 != columns2) {
		cout << "Неверное значение строк и столбцов матриц!" << endl;
		system("pause");
		exit(-1);
	}

	SparseMatrixClass Result(rows1, columns1);

	int* ResValues = new int[Result.Columns()];

	for (int row = 0; row < matrix1.JR.size(); row++) {
		int next1 = matrix1.JR[row];
		int next2 = matrix2.JR[row];

		for (int i = 0; i < Result.Columns(); i++)
			ResValues[i] = 0;

		if (next1 != -1 && next2 != -1) {
			//Finding all values and columns for the first matrix;
			do {
				int col1 = -1;
				for (int i = 0; i < matrix1.JC.size(); i++)
					if (matrix1.JC[i] == next1)
						col1 = i;
				if (col1 == -1) {
					int nextCol1 = matrix1.NC[next1];
					while (nextCol1 != next1) {
						for (int j = 0; j < matrix1.JC.size(); j++)
							if (matrix1.JC[j] == nextCol1)
								col1 = j;
						nextCol1 = matrix1.NC[nextCol1];
					}
				}
				ResValues[col1] += matrix1.AN[next1];
				next1 = matrix1.NR[next1];
			} while (next1 != matrix1.JR[row]);
			do {
				int col2 = -1;
				for (int k = 0; k < matrix2.JC.size(); k++)
					if (matrix2.JC[k] == next2)
						col2 = k;
				if (col2 == -1) {
					int nextCol2 = matrix2.NC[next2];
					while (nextCol2 != next2) {
						for (int z = 0; z < matrix2.JC.size(); z++)
							if (nextCol2 == matrix2.JC[z])
								col2 = z;
						nextCol2 = matrix2.NC[nextCol2];
					}
				}
				ResValues[col2] += matrix2.AN[next2];
				next2 = matrix2.NR[next2];
			} while (next2 != matrix2.JR[row]);

			for (int i = 0; i < Result.Columns(); i++)
				if (ResValues[i] != 0)
					Result.Add(ResValues[i], row, i);
		}
		else if (next1 != -1 && next2 == -1) {
			do {
				int col1 = -1;
				for (int i = 0; i < matrix1.JC.size(); i++)
					if (matrix1.JC[i] == next1)
						col1 = i;
				if (col1 == -1) {
					int nextCol1 = matrix1.NC[next1];
					while (nextCol1 != next1) {
						for (int j = 0; j < matrix1.JC.size(); j++)
							if (matrix1.JC[j] == nextCol1)
								col1 = j;
						nextCol1 = matrix1.NC[nextCol1];
					}
				}
				ResValues[col1] += matrix1.AN[next1];
				next1 = matrix1.NR[next1];
			} while (next1 != matrix1.JR[row]);
			for (int i = 0; i < Result.Columns(); i++)
				if (ResValues[i] != 0)
					Result.Add(ResValues[i], row, i);
		}
		else if (next1 == -1 && next2 != -1) {
			do {
				int col2 = -1;
				for (int k = 0; k < matrix2.JC.size(); k++)
					if (matrix2.JC[k] == next2)
						col2 = k;
				if (col2 == -1) {
					int nextCol2 = matrix2.NC[next2];
					while (nextCol2 != next2) {
						for (int z = 0; z < matrix2.JC.size(); z++)
							if (nextCol2 == matrix2.JC[z])
								col2 = z;
						nextCol2 = matrix2.NC[nextCol2];
					}
				}
				ResValues[col2] += matrix2.AN[next2];
				next2 = matrix2.NR[next2];
			} while (next2 != matrix2.JR[row]);
			for (int i = 0; i < Result.Columns(); i++)
				if (ResValues[i] != 0)
					Result.Add(ResValues[i], row, i);
		}
	}
	delete ResValues;
	Result.Boxing();
	Result.Reset();
	return Result;
}


int main(void) {
	SetRussian();
	
	const int RANGE_VALUE = 10;
	SparseMatrixClass Matrix1; SparseMatrixClass Matrix2;
	char ch;
	int row, column;
	int value;
	double rarefaction;

	cout << "Введите количество строк матрицы 1: ";
	cin >> row ;
	cout << "Введите количество столбцов матрицы 1: ";
	cin >> column;
	SparseMatrixClass matrix1(row, column);

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < column; j++) {
			cout << "Item [" << i << "][" << j << "]: ";
			cin >> value;
			matrix1.Add(value, i, j);
		}
	}
	matrix1.Boxing();
	Matrix1 = matrix1;

	cout << "Введите количество строк матрицы 2: ";
	cin >> row;
	cout << "Введите количество столбцов матрицы 2: ";
	cin >> column;
	SparseMatrixClass matrix2(row, column);

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < column; j++) {
			cout << "Item [" << i << "][" << j << "]: ";
			cin >> value;
			matrix2.Add(value, i, j);
		}
	}
	matrix2.Boxing();
	Matrix2 = matrix2;
	

	SparseMatrixClass resultAdd, resultMul;

	cout << "СЛОЖЕНИЕ:" << endl;
	resultAdd = Addition(Matrix1, Matrix2);
	Output(resultAdd, Matrix1, Matrix2);

	cout << "УМНОЖЕНИЕ:" << endl;
	resultMul = Multiplication(Matrix1, Matrix2);
	Output(resultMul, Matrix1, Matrix2);


	system("pause");
	return 0;
}


void Output(SparseMatrixClass& result, SparseMatrixClass& matrix1, SparseMatrixClass& matrix2) {
	cout << "-----------------------------" << endl;
	cout << "\tУпаковка матрицы 1: " << endl;
	cout << "-----------------------------" << endl;
	matrix1.ShowBoxing();
	cout << "-----------------------------" << endl;
	cout << "-----------------------------" << endl;
	cout << "\tУпаковка матрицы 2:" << endl;
	cout << "-----------------------------" << endl;
	matrix2.ShowBoxing();
	cout << "-----------------------------" << endl;
	cout << "\tРезультат: " << endl;
	cout << "-----------------------------" << endl;
	result.ShowBoxing();
	cout << "-----------------------------" << endl;
	cout << "\tРезультат распакованный: " << endl;
	result.ShowMatrix();
	cout << "-----------------------------" << endl;
}