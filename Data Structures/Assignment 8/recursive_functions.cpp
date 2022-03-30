#include <iostream>
#include <string>
using namespace std;

//*****************************************************************************
//P R O G R A M	H E A D E R
//
//	Name: Jordan Diaz
//	Z#:	Z23554771
//	Instructor:	Dr. Bullard
//	Class:	Data Structures
//	Term:	Spring 2021
//	Assignment #8 (recursion functions)
//	Due Date:	March 26, 2021
//	Due Time:	11:59PM
//	Points:	25
//
//	Description: This program accesses your C++language skills.
//	After completing this assignment you will be able to perform the following:
//
//	(1) Write Recursive functions
//	(2) write iterative functions
//******************************************************************************


///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: palindrome
//Precondition: user entered string
//Postcondition: string has been checked if is palindrome
//Description: Returns true or false based on if a string is a palindrome or not
///////////////////////////////////////////////////////////////////////////////////////////////
bool palindrome(string& s)
{
	string palindromeString;
	if (s.length() == 1 || s.length() == 0) //if length of string is 0 or 1
	{
		return true;
	}
	else if (s[0] == s[s.length() - 1]) //if the first character and the last character are the same
	{
		palindromeString = s.substr(1, s.length() - 2); // removes the front and back of string
		return palindrome(palindromeString); //calls the function again
	}
	else //otherwise it is false
	{
		return false;
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: palindrome
//Precondition: user entered string
//Postcondition: string has been reversed recursively
//Description: Returns the reversed string recursively
///////////////////////////////////////////////////////////////////////////////////////////////
string printReversel(string& s)
{
	if (s.length() == 1 || s.length() == 0)
	{
		return s;
	}
	else
	{
		string updatedString = s.substr(0, s.length() - 1); //store the string with one less character at the end, apple becomes appl
		return s[s.length() - 1] + printReversel(updatedString); //call the function again while also adding the last character of the string
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: printIterReverse
//Precondition: user entered string
//Postcondition: string has been reversed iteratively
//Description: Returns a reversed string iteratively
///////////////////////////////////////////////////////////////////////////////////////////////
string printIterReverse(string& s)
{
	string reversedString;
	for (int i = s.length() - 1; i >= 0; i--) //start at the back, continue as long as i is greater or equal to zero, decrement
	{
		reversedString += s[i]; //add the current index to the string
	}
	return reversedString;
}

int main()
{
	string s = "";
	string response = "y";

	while (response == "y" || response == "Y")
	{
		cout << "please enter string: ";
		getline(cin, s);
		if (palindrome(s) == true)
		{
			cout << s << " is a palindrome \n";
		}
		else
		{
			cout << s << " is not a palindrome \n";
		}

		cout << "The Rec-reverse of \"" << s << "\" is \"" << printReversel(s) << "\"" << endl;
		cout << "The Iter-reverse of \"" << s << "\" is \"" << printIterReverse(s) << "\"" << endl;
		cout << endl << "Do you wish to continue (y or Y for yes; n or N for no? ";

		cin >> response;
		cin.ignore();
	}

	return 0;
}

