// Jordan Diaz
// Cop 3014
// This program finds and prints all of the prime numbers between 3 and x (x is user input)

#include <iostream>

using namespace std;

int main()
{
	int userInput, output, divisor, tested = 0, currentPrime, currentValue; 
	bool isPrime;

	cout << "Please enter a Positive Whole Number greater than or equal to 2: ";
	cin >> userInput;
	
	 if (userInput >= 2)
	 {
		 cout << endl;
		 cout << "2";

		 for (currentValue = 1; currentValue <= userInput; currentValue++) // increment the current value
		 {
			 isPrime = true;

			 for (divisor = 2; divisor < currentValue; divisor++) // Contintues to check if prime
			 {
				 output = currentValue % divisor; // prime calculation

				 if (output == 0) // if not prime
				 {
					 divisor = userInput;
					 isPrime = false;
				 }

				 else if (output > 0) // sum of outputs 0
				 {
					 tested += output;
				 }

			 }
			 
			 if (tested != 0 && isPrime) // if prime
			 {
				 currentPrime = currentValue;
				 cout << " " << currentPrime;
			 }

		 }

		 cout << endl <<endl << "These are the prime numbers inbetween 2 and " << currentValue - 1 << endl;
	 }
	 else
	 {
		cout << endl << "You have entered an invalid input, please restart program: \n";
	 }

	return 0;
}