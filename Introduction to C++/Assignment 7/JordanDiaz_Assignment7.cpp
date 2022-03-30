//Jordan Diaz
//Cop 3014
//This program will emulate a grading system with weights

#include <iostream>
#include <string>

using namespace std;

const int NUMBER_STUDENTS = 2, NUMBER_TESTS = 4;

class studentRecord
{
public:
	studentRecord();//Default Contructor //Constructor that initializes to set values
	void setGrades(double a[],int NUMBER_TESTS);//set each of member variables to values given as an argument to the function
	void getGrades(double b[], int NUMBER_TESTS);//member function to retrieve the data from each of the member variable
	double CalculateAvg();//Calculates the weighted average numeric score for the entire course and sets the corresponding member variable
	void CalculateFinalScore();// void function that calculates the students final grades and sets the corresponding member variable

private:
	double quiz1,quiz2,midterm,final;
	double finalScore;
	double universalArr[4] = {0.0,0.0,0.0,0.0};
	char finalLetterGrade;
};

studentRecord student1;
studentRecord student2;

studentRecord::studentRecord(): quiz1(0.0), quiz2(0.0),midterm(0.0),final(0.0)
{
}

void studentRecord::setGrades(double a[], int NUMBER_TESTS)
{
	for (int i = 0; i < NUMBER_TESTS; i++)
	{
		string TestNumber[] = { "Quiz1?: ", "Quiz2?: ", "the Midterm?: ","the Final?: " };
		int NumberOfPoints[] = { 20,20,100,100 };
		cout << endl <<"Out of "<< NumberOfPoints[i] << " points, how many points did you get on " << TestNumber[i];
		cin >> a[i];
		universalArr[i] = a[i];
	}
	student1.getGrades(a, 4);
	student2.getGrades(a, 4);
}

void studentRecord::getGrades(double b[], int NUMBER_TESTS)
{
	quiz1 = b[0];
	quiz2 = b[1];
	midterm = b[2];
	final = b[3];
}

double studentRecord::CalculateAvg()
{
	// Percentages
	double q1p = (quiz1 / 20) * 100; 
	double q2p = (quiz2 / 20) * 100;
	double mp = (midterm / 100) * 100;
	double fp = (final / 100) * 100;
	cout << endl << "Your score on Quiz1 was: " << q1p << "%";
	cout << endl << "Your score on Quiz2 was: " << q2p << "%";
	cout << endl << "Your score on the Midterm was: " << mp << "%";
	cout << endl << "Your score on the Final was: " << fp << "%";
	// Calculations
	finalScore = (q1p * 20 + q2p * 20 + mp * 25 + fp * 35)/(40+25+35);
	cout << endl << finalScore << " ";

	return finalScore;
}
void studentRecord::CalculateFinalScore()
{
	if (finalScore >= 90.0)
	{
		finalLetterGrade = 'A';
	}
	else if (finalScore >= 80.0 && finalScore < 90.0)
	{
		finalLetterGrade = 'B';
	}
	else if (finalScore >= 70.0 && finalScore < 80.0)
	{
		finalLetterGrade = 'C';
	}
	else if (finalScore >= 60.0 && finalScore < 70.0)
	{
		finalLetterGrade = 'D';
	}
	else if (finalScore < 60)
	{
		finalLetterGrade = 'F';
	}
	cout << finalLetterGrade;
}

int main()
{
	double student1Score, student2Score;
	double StoreStudent1[4];
	double StoreStudent2[4];
	double arr[4];
	cout <<  "Student one, it is your turn to enter your scores\n";
	student1.setGrades(StoreStudent1, 4);
	
	cout << endl << "Student1 Scores:";
	student1Score = student1.CalculateAvg();
	student1.CalculateFinalScore();
	
	cout << endl << endl << "Student two, it is your turn to enter your scores\n";
	student2.setGrades(StoreStudent2, 4);
	
	cout << endl << "Student2 Scores";
	student2Score = student2.CalculateAvg();
	student2.CalculateFinalScore();

	cout << endl;

	if (student1Score > student2Score)
	{
		cout << endl << "Student one scored higher in the class" << endl;
	}
	else if (student1Score < student2Score)
	{
		cout << endl << "Student two scored higher in the class" << endl;
	}
	else if (student1Score == student2Score)
	{
		cout << endl << "Both students scored the same grade" << endl;
	}

	return 0;
}