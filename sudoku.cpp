//============================================================================
// Name        : sudoku.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Sudoku in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

void printSudoku(int a[9][9])
{
	for(int i=0;i<9;i++)
	{
		for(int j = 0;j<9;j++)
		{
			cout<<a[i][j]<<" ";
		}
		cout<<endl;
	}
}

bool isValidPos(int a[9][9], int r,int c, int val)
{
	for(int i=0;i<9;i++)
	{
		if(a[r][i] == val)
			return false;
	}
	for(int j=0;j<9;j++)
	{
		if(a[j][c] == val)
			return false;
	}
	int row = r/3;
	int col = c/3;
	for(int i = 3*row;i<3*(row+1);i++)
	{
		for(int j = 3*col;j<3*(col+1);j++)
		{
			if(a[i][j] == val)
				return false;
		}
	}
	return true;
}

bool findEmpty(int a[9][9],int &row, int& col)
{
	for(int i=0;i<9;i++)
	{
		for(int j = 0;j< 9; j++)
		{
			if(a[i][j] == 0)
			{
				row = i;
				col = j;
				return 1;
			}
		}
	}
	return 0;
}

bool solve(int a[9][9])
{
	int row, col;
	if(!findEmpty(a,row,col))
		return true;
	for(int j=1;j<=9;j++)
	{
		if(isValidPos(a,row,col,j))
		{
			a[row][col] = j;
			if(solve(a))
				return true;
			a[row][col] = 0;
		}
	}
	return false;
}

int main() {
	int a[9][9] = {{4,0,9,0,0,8,0,3,0},
				   {7,5,0,0,3,2,0,1,8},
				   {0,0,0,5,0,0,2,0,6},
				   {8,0,0,0,0,3,9,0,0},
				   {0,3,0,0,4,0,0,7,5},
				   {0,0,1,2,0,7,0,0,0},
				   {0,0,8,4,0,0,0,0,9},
				   {0,1,0,0,0,9,0,4,0},
				   {2,0,0,7,1,0,8,5,0}};
	cout<<"Original Matrix :- "<<endl;
	printSudoku(a);
	bool ch = solve(a);
	if(ch == 0)
		cout<<"\nNo Solution possible"<<endl;
	else
	{
		cout<<"\nSOLUTION :- "<<endl;
		printSudoku(a);
	}

	return 0;
}
