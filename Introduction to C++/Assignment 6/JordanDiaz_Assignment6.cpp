// Cop3014
// Jordan Diaz
// This program reads integer data from the keyboard until end of file is reached
// also counts how many positive and negative integers are read
#include <iostream>
#include <fstream>

using namespace std;

class LetsCount {
public:
	void SetCounter(int number); // sets the counter to the value specified by the argument
	void CountUp(); // increase count by 1
	void CountDown(); // decrease count by 1 (Cannot subtract so that counter becomes negative)
	int GetCount(); // Returns the current count
	void Output(); // Outputs the count to the screen ()
private:
	int count;
	int positiveCount;
	int negativeCount;
};

int main()
{
	LetsCount PositiveIntegers; // starts at zero and counts positive ints
	LetsCount NegativeIntegers; // starts at total number of integers user and minus the counter for every positive

	PositiveIntegers.SetCounter(0);
	NegativeIntegers.SetCounter(0);

	int UserInput, total;

	ifstream readInput;
	ofstream writeOutput;

	writeOutput.open("ListOfIntegers.txt");

	do
	{
		cout << "Enter a value to continue or press 0 to get results ";
		cin >> UserInput;

		if (UserInput > 0)
		{
			PositiveIntegers.CountUp();
		}
	
		NegativeIntegers.CountUp();

		if (UserInput != 0)
		{
			writeOutput << UserInput << endl;
		}

	} while (UserInput != 0);

	writeOutput.close();

	readInput.open("ListOfIntegers.txt");

	total = NegativeIntegers.GetCount() - 1;

	NegativeIntegers.SetCounter(total);

	int next;
	while (readInput >> next)
	{
		if (next > 0)
		{
			NegativeIntegers.CountDown();
		}
	}

	cout << endl << "there were ";  PositiveIntegers.Output(); 

	cout << " positive integers and "; NegativeIntegers.Output();

	cout << " negative integers and there was a total of " << total << " integers" << endl;

	readInput.close();

	return 0;
}

void LetsCount::SetCounter(int number) { count = number; }

void LetsCount::CountUp() { count ++; }

void LetsCount::CountDown()
{
	if (count > 0)
	{
		count--;
	}
}

int LetsCount::GetCount() { return count; }

void LetsCount::Output() { cout << count; }
// I wanted exactly 100 lines of code :)