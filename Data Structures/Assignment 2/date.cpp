#include <iostream>
#include <string>
#include <iomanip>
#include "date.h"

using namespace std;

//*************************************************************************************
//Name:	Date
//Precondition: The state of the object (private data) has not been initialized
//Postcondition: The state has been initialized to today's date
//Description:	This is the default constructor which will be called automatically when
//an object is declared.	It will initialize the state of the class
//
//*************************************************************************************
Date::Date() //default constructor; sets m = 01, d = 01, y = 0001
{
	myMonth = 1;
	myDay = 1;
	myYear = 0001;
	cout << "Default Constructor has been called\n";
	display();
}

//*************************************************************************************
//Name:	explicit-value constructor (Overload Date)
//Precondition: myMonth, myDay, and myYear has not been given the value from the driver
//Postcondition: myMonth, myDay, and myYear has been given the value from the driver, successful overload
//Description: explicit-value constructor to set date equal to today's in the driver
//
//*************************************************************************************
Date::Date(unsigned m, unsigned d, unsigned y) // unsigned integers are non-negative whole numbers only, can store 256 values
{
	// The unsigned integers makes it so that the person controlling the driver won't put a negative sign or decimal for the date
	myMonth = m;
	myDay = d;
	myYear = y;
	cout << endl << "Explicit-value Constructor has been called\n";
	display();
}

//*************************************************************************************
//Name:	Display
//Precondition: The private data has not been displayed
//Postcondition: The private data has been printed to the screen with proper formatting
//Description: output Date object to the screen 
//
//*************************************************************************************
void Date::display()
{
	//7 months have 31 days: Jan, Mar, May, Jul, Aug, Oct, Dec
	//a leap year is on a feb with the day of 29 and a year that ends in 0,4,6,8

	bool badMonth = 0, BadDay = 0, BadYear = 0, LeapYear = 0;

	// Check for bad months, days, year, and leap year
	if ((myMonth == 2 && myDay == 29 && ((myYear % 10 == 0) || (myYear % 10 == 4) ||
		(myYear % 10 == 6) || (myYear % 10 == 8))))
	{
		LeapYear = true;
		cout << setfill('0') << setw(2) << myMonth << "\\" << setw(2) << myDay << "\\" << setfill('0') << setw(4) << myYear << endl;
		cout << "This is a leap year" << endl;
	}
	if ((myMonth <= 0) || (myMonth > 12)) { cout << "Month = " << myMonth << " is incorrect" << endl; badMonth = true; }//Check for bad month
	if ((myDay <= 0) || (myDay > 31)) { cout << "Day = " << myDay << " is incorrect" << endl; BadDay = true; }//Check for bad day
	if (!(myYear > 0)) { cout << "Year = " << setw(4) << myYear << " is incorrect" << endl; BadYear = true; }//Check for bad year
	if (myMonth == 2 && myDay > 29) { cout << "Day = " << myDay << " is incorrect" << endl; BadDay = true; }//Check for another bad day
	if (BadDay && badMonth && BadYear) { cout << endl; }
	if (!(BadDay || badMonth || BadYear || LeapYear))
	{
		cout << setfill('0') << setw(2) << myMonth << "\\" << setw(2) << myDay << "\\" << setfill('0') << setw(4) << myYear << endl;
	}	
}

//*************************************************************************************
//Name:	getMonth
//Precondition: The month has not been accessed
//Postcondition: The month has been accessed and returned
//Description: accessor to output the month
//
//*************************************************************************************
int Date::getMonth() //accessor to output the month 
{
	cout << endl;
	return myMonth;
}

//*************************************************************************************
//Name:	getDay
//Precondition: The Day has not been accessed
//Postcondition: The Day has been accessed and returned 
//Description: accessor to output the day 
//
//*************************************************************************************
int Date::getDay()
{
	return myDay;
}

//*************************************************************************************
//Name:	getYear
//Precondition: The Year hasnt been accessed
//Postcondition: The year has been accessed and returned
//Description: accessor to output the year
//
//*************************************************************************************
int Date::getYear()
{
	return myYear;
}

//*************************************************************************************
//Name: setMonth
//Precondition: The value of myMonth has not been set
//Postcondition: myMonth has been set to the unsigned integer m
//Description: mutator to change the month
//
//*************************************************************************************
void Date::setMonth(unsigned m)
{
	myMonth = m;
}

//*************************************************************************************
//Name:	setDay
//Precondition: The value of myDay has not been set 
//Postcondition: myDay has been set to the unsigned integer d
//Description: mutator to change the day
//
//*************************************************************************************
void Date::setDay(unsigned d)
{
	myDay = d;
}

//*************************************************************************************
//Name:	setYear
//Precondition: The value of myDay has not been set
//Postcondition: myYear has been set to the unsigned integer y
//Description: mutation to change the year
//
//*************************************************************************************
void Date::setYear(unsigned y)
{
	myYear = y;
}

//*************************************************************************************
//Name:	operator
//Precondition: objects from the date class cannot chain 
//Postcondition: objects from the date class can now return the private data from calling the whole object (chaining )
//Description: overloaded operator<< as a friend function with chaining
// Allows for the date to be called by only outputting the name of the object
//
//*************************************************************************************
ostream& operator<<(ostream& out, Date& dateObj) // Allows for the date to be called by only outputting the name of the object
{
	out << setfill('0') << setw(2) << dateObj.myMonth << "\\" << setw(2) << dateObj.myDay << "\\" << setfill('0') << setw(4) << dateObj.myYear;

	return out;
}