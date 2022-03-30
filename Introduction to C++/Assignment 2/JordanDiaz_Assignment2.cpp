//This program was written by Jordan Diaz on 9/16/2020 for COP3014

#include <iostream>
using namespace std;

int main()
{
	int CurrentNum, Counter, PositiveSum, NonPositiveSum, TotalSum, TotalNum, NumberOfPositive, NumberOfNonPositive;
	double TotalAvg, PositiveAvg, NonPositiveAvg;

	//Initialization of Variables
	NumberOfNonPositive = 0;
	NumberOfPositive = 0;
	NonPositiveSum = 0;
	NonPositiveAvg = 0;
	PositiveSum = 0;
	PositiveAvg = 0;
	TotalNum = 0;
	TotalSum = 0;
	Counter = 0;

	// Displays input and output, progresses through loop, and increments
	while (Counter < 10)
	{
		cout << "Enter a number: ";

		if (Counter < 10) { 
			cin >> CurrentNum;

			if (CurrentNum > 0)
			{
				PositiveSum += CurrentNum;
				NumberOfPositive ++;
			}
			else
			{
				NonPositiveSum += CurrentNum;
				NumberOfNonPositive ++;
			}
		}
		TotalSum += CurrentNum;
		TotalNum++;
		Counter++;
	}
	//Set decimal points
	cout.setf(ios::fixed); 
	cout.setf(ios::showpoint); 
	cout.precision(2);

	//Math and Final Output for positive numbers
	if (NumberOfPositive > 0)
	{
		PositiveAvg = static_cast <double>(PositiveSum) / NumberOfPositive;

		cout << endl << "The Positive Sum is: " << PositiveSum;
		cout << endl << "The Positive Average is: " << PositiveAvg;
	}
	else
	{
		cout << endl << "There are no Positive Numbers";
	}

	//Math and Final output for the Non-Positive numbers
	if (NumberOfNonPositive > 0)
	{
		NonPositiveAvg = static_cast <double>(NonPositiveSum) / NumberOfNonPositive;

		cout << endl << "The Non-Positive Sum is: " << NonPositiveSum;
		cout << endl << "The Non-Positive Average is: " << NonPositiveAvg;
	}
	else
	{
		cout << endl << "There are no Non-Positive Numbers";
	}
	
	TotalAvg = static_cast <double>(TotalSum) / TotalNum;

	cout << endl << "The Total Sum is: " << TotalSum;
	cout << endl << "The Total Average is: " <<TotalAvg;
	cout << endl;

	return 0;
}
