#include <iostream>
#include <vector>

using namespace std;

class SparseMatrixClass {
private:
	int rows;
	int columns;
	int** Matrix;
public:
	vector<int> AN;
	vector<int> NR;
	vector<int> NC;
	vector<int> JR;
	vector<int> JC;

	SparseMatrixClass();
	SparseMatrixClass(int, int);
	SparseMatrixClass(const SparseMatrixClass&);
	SparseMatrixClass& operator=(const SparseMatrixClass&);
	void Add(int, int, int);
	void Boxing(void);
	void UnBoxing(void);
	void Reset(void) {
		if (Matrix != nullptr) {
			for (int i = 0; i < rows; i++)
				delete Matrix[i];
			delete Matrix;
		}
		rows = 0; columns = 0;
		Matrix = nullptr;
	}
	int Rows(void) {
		return rows;
	}
	int Columns(void) {
		return columns;
	}
	void ShowMatrix(void);
	void ShowBoxing(void);
	~SparseMatrixClass() {
		if (Matrix != nullptr) {
			for (int i = 0; i < rows; i++)
				delete Matrix[i];
			delete Matrix;
		}
	}
};



