// Jordan Diaz
// COP 3014		10/24/2020
// This program generates a file of random numbers, and then prints them in neat fashion to another file
// finds average and standard deviation 

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <cmath>

using namespace std;

// Functions
void Random_Input(ofstream& outfile); // Generates file of random numbers that consits of N numbers
void makeneat(ifstream& messy, ofstream& neat, int precision, int width); // handles formatting
double Averages(ifstream& infile, ofstream& outfile, int file_size); // calculates average
void StdDeviation(ifstream& infile, ofstream& outfile, double average, int file_size); // calculates std deviation

int main()
{
	ifstream readInput;
	ofstream writeOutput;

	makeneat(readInput, writeOutput, 6, 10);

	Random_Input(writeOutput);

	double avg = Averages(readInput, writeOutput, 0);

	StdDeviation(readInput, writeOutput, avg, 0);
}

void Random_Input(ofstream& outfile)
{
	int numbersGenerated = 0;

	srand(time(NULL));

	// (0 to 898) + 101 = 101 to 999, which are the values inbetween 100 and 1000 (Generates N)
	int NumbersToBeGenerated = (rand() % 898) + 101;

	outfile.open("Results.txt");

	// Generates N values between 0 and 50
	for (numbersGenerated = 0; numbersGenerated < NumbersToBeGenerated; numbersGenerated++)
	{
		double generatedNumber = 50 * (double)rand() / RAND_MAX;

		outfile << setw(10) << right << generatedNumber << endl;
	}

	outfile << endl << "There were " << NumbersToBeGenerated << " values generated";

	outfile.close();

}

void makeneat(ifstream& messy, ofstream& neat, int precision, int width)
{
	neat.setf(ios::fixed);
	neat.setf(ios::showpoint);
	neat.setf(ios::showpos);
	neat.precision(precision);
}

double Averages(ifstream& infile, ofstream& outfile, int file_size)
{
	infile.open("Results.txt");

	double next, sum = 0;
	int count = 0;
	while (infile >> next)
	{
		sum += next;
		count++;
	}

	double average = sum / count;

	infile.close();

	outfile.open("Results.txt", ios::app);

	outfile << endl << "The average is " << average;

	cout << endl << "The average is " << average << endl;

	outfile.close();

	return average;
}

void StdDeviation(ifstream& infile, ofstream& outfile, double average, int file_size)
{
	infile.open("Results.txt");

	double next, sum = 0;
	int count = 0;
	while (infile >> next)
	{
		sum += ((next - average) * (next - average));
		count++;
	}

	double stdDeviation = sqrt(sum/count);

	infile.close();

	outfile.open("Results.txt", ios::app);

	outfile << endl << "the standard deviation is " << stdDeviation;
	cout << endl << "the standard deviation is " << stdDeviation << endl;

	outfile.close();
}