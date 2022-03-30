//This program was written by Jordan Diaz on 9/3/2020

#include<iostream>
using namespace std;

int main()
{
	//Variables
	//Stores the user input and logic into these variables
	int Quarters, Dimes, Nickels, Total;

	//print text to the console (Output and Input)
	cout << "How Many Quarters? : ";
	cin >> Quarters;
	cout << endl << "How Many Dimes? : ";
	cin >> Dimes;
	cout << endl << "How many Nickels? : ";
	cin >> Nickels;

	//Logic
	Total = (Quarters * 25) + (Dimes * 10) + (Nickels * 5);

	//Final text
	cout << endl << "You have a total of " << Total << " Cents" << endl;

	return 0;
}