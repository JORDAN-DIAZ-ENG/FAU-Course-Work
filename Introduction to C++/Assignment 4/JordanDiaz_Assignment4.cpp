// Jordan Diaz
// Cop 3014
// 10/11/20
// This program converts a value of cents into Quarters, Dimes, Nickels, and Pennies

#include <iostream>

using namespace std;

// Functions
void Input(int &UserInput); // Reads input values from 1 to 99
int Calculate(int &ValueInCents, int &QuartersUsed, int &DimesUsed, int &NickelsUsed, int &PenniesUsed); // Caclulates the number of coins for each denomination
void Output(int ValueInCents, int QuartersUsed, int DimesUsed, int NickelsUsed, int PenniesUsed); // Outputs the values
void Repeat(bool &Continue); // This lets the program loop

// CONSTANTS
const int QUARTERS = 25, DIMES = 10, NICKELS = 5, PENNIES = 1;

int main()
{
	bool Repeating = true;

	while (Repeating)
	{
		int UserChange, totalQuarters, totalDimes, totalNickels, totalPennies;

		Input(UserChange);

		Calculate(UserChange, totalQuarters, totalDimes, totalNickels, totalPennies);

		Output(UserChange, totalQuarters, totalDimes, totalNickels, totalPennies);

		Repeat(Repeating);
	}
}

void Input(int &UserInput)
{
	cout << " ~~~~~ Welcome to the ATM we take change from 1 to 99 cents ~~~~~ \n";

	cout << endl << " Enter the amount of change you have from 1 to 99 cents: ";

	cin >> UserInput;
	cout << endl;

	while (UserInput > 99 || UserInput < 1)
	{
		cout << endl << "Please Enter the amount of change you have from 1 to 99 cents: ";
		cin >> UserInput;
	}
}

int Calculate(int &ValueInCents, int &QuartersUsed, int &DimesUsed, int &NickelsUsed, int &PenniesUsed)
{
	double RemainingCents;

	//Calculation
	QuartersUsed = ValueInCents / QUARTERS;
	RemainingCents = ValueInCents % QUARTERS;

	DimesUsed = RemainingCents / DIMES;
	RemainingCents -= (DimesUsed * DIMES);

	NickelsUsed = RemainingCents / NICKELS;
	RemainingCents -= (NickelsUsed * NICKELS);

	PenniesUsed = RemainingCents / PENNIES;

	return 0;
}

void Output(int ValueInCents,int QuartersUsed, int DimesUsed, int NickelsUsed, int PenniesUsed)
{
	cout << ValueInCents << " cents can be given as:" << endl;
	cout << endl << QuartersUsed << " Quarter(s) " << DimesUsed << " Dime(s) " << NickelsUsed << " Nickel(s) and " << PenniesUsed << " Penny(s)" << endl;
}

void Repeat(bool &Continue)
{
	int UserValue;
	cout << endl << "Would you like to try another value? \n";
	cout << endl << "1 for yes, 0 for no: ";
	cin >> UserValue;
	cout << endl;

	if (UserValue == 1)
	{
		Continue = true;
	}
	else if (UserValue == 0)
	{
		Continue = false;
	}
}