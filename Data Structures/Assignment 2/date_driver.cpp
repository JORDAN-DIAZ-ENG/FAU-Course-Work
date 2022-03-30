#include <iostream>
#include <string>
#include <iomanip>
#include "date.h"

using namespace std;

// PROGRAM HEADER
/********************************************************************************************

Name:	Jordan Diaz		Z#:	Z23554771
Course: Date Structures and Algorithm Analysis (COP3530) Professor: Dr. Lofton Bullard
Due Date:	1/29/2021	Due Time:	11:59pm
Total Points: 25 Assignment 2: Date program

Description: This program uses a collection of set, get, display, and friend functions to a date based on the driver



*********************************************************************************************/

int main()
{
	Date myDate;
	Date herDate(11, 14, 1953);
	Date test1Date(25, 1, 1982); //should generate error message that bad month
	Date test22Date(2, 29, 2020); //ok, should say leep year
	Date test3Date(2, 30, 2021); //should generate error message that bad day
	Date test4Date(1, 25, 0000); //should generate error message that bad year
	Date test5Date(80, 40, 0000); //should generate error message that bad month, day and year

	herDate.display();
	cout << herDate.getMonth() << endl;
	cout << herDate.getDay() << endl;
	cout << herDate.getYear() << endl;
	myDate.setMonth(11);
	myDate.setDay(12);
	myDate.setYear(2015);
	cout << "myDate: " << myDate << " test22Date: " << test22Date << " herDate: " << herDate << endl;

	return 0;
}