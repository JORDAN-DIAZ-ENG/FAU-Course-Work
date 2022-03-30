#include <iostream>
#include <fstream>
#include <string>
#include "string_class.h"
using namespace std;

//*************************************************************************************
//Name:	string_class (default constructor)
//Precondition: current_string has not been assigned a value
//Postcondition: current_string has been given the value of ""
//Description:  default constructor called by default once an object is instantiated
//
//*************************************************************************************
string_class::string_class() //default constructor;
{
	current_string = "";
}

//*************************************************************************************
//Name:	string_class (explicit-value constructor)
//Precondition: current_string has not been assigned a value
//Postcondition: current_string has been given the value from the argument in the driver
//Description:	explicit-value constructor called by overloading an object with a string
//
//*************************************************************************************
string_class::string_class(string arg)
{
	current_string = arg;
}

//*************************************************************************************
//Name:	palindrome
//Precondition: true or false has not been returned
//Postcondition: true or false has been returned based on there being a palindrome or not
//Description: checks if a string is read the same forward and backward
//
//*************************************************************************************
bool string_class::palindrome()
{
	string RightToLeft = "", LeftToRight = "", RightToLeftCAPS = "", LeftToRightCAPS = "";

	// current_string.length() - 1 because without the -1 there would be a space
	for (int i = current_string.length() - 1 ; i >= 0; i--) // Direction:Right to Left
	{
		RightToLeft += current_string[i];
	}
	// Direction:Left to Right is already given
	LeftToRight = current_string; 

	// give values to be modified
	RightToLeftCAPS = RightToLeft;
	LeftToRightCAPS = LeftToRight;
	
	// modify values to all caps so that the check is case sensitive
	for (int i = 0; i < RightToLeftCAPS.length(); i++)
	{
		RightToLeftCAPS[i] = toupper(RightToLeftCAPS[i]);
	}
	for (int i = 0; i < LeftToRightCAPS.length(); i++)
	{
		LeftToRightCAPS[i] = toupper(LeftToRightCAPS[i]);
	}

	// Palindrome Check
	if (RightToLeftCAPS == LeftToRightCAPS)
	{
		return true;
	}
	return false;
}

//*************************************************************************************
//Name:	replace_all
//Precondition: string has not been altered
//Postcondition: current_string's old_substrings have been replaced with new_substrings
//Description:	Mutator that checks every character in a string for a substring then removes and inserts, some special cases
//
//*************************************************************************************
void string_class::replace_all(string old_substring, string new_substring) 
{
	string temp, safety, final;
	int oldSize = old_substring.length();
	bool Exists = false;

	//special cases
	safety += current_string;

	if (old_substring.length() > current_string.length())
	{
		bool Exists = false;
	}
	else
	{
		// change current string
		for (int i = 0; i < current_string.length(); i++)
		{
			temp = current_string[i];
			
			for (int j = 1; j < oldSize; j++)
			{
			
				//cout << "This is run 2";
				if (!(i + j > current_string.length()))
				{
					temp += current_string[i + j];
				}
				
				if (temp == old_substring)
				{
					Exists = true;

					for (int k = 0; k < oldSize; k++)
					{
						current_string.erase(current_string.begin() + i);
					}
					current_string.insert(i, new_substring);
						i += oldSize;
					final = current_string;
				}
				
			}
			
			if (new_substring.empty())
			{
				if (oldSize <= 1)
				{	
				if (current_string.at(i) != old_substring[0]) { final += current_string.at(i); Exists = true;}
				}
			}
		}
	}
	current_string = final;
	if (Exists == false){ current_string = safety; }
}

//*************************************************************************************
//Name:	operator
//Precondition: has not returned the private members of the string_class Object
//Postcondition: has returned the private members of the string_claass Object
//Description: overloaded operator<< as a friend function with chaining
//
//*************************************************************************************
ostream& operator<<(ostream& out, string_class& string_classObj)
{
	out << string_classObj.current_string;
	return out;
}