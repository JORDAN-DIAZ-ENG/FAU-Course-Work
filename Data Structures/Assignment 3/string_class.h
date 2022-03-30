#pragma once

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class string_class
{
public:
	//Constructors
	string_class(); // default constructor, sets current_string to an empty string ("")
	string_class(string arg); // explicit-value constructor, sets "current_string" equal to the argument that is passed to the explicit-value constructor when a string_class object is delcared

	//Member Functions
	bool palindrome(); // returns true if palindrome, returns false otherwise
	void replace_all(string old_substring, string new_substring); // replaced oldstring with newstring in current string

	friend ostream& operator<<(ostream& out, string_class& string_classObj);//overloaded operator<< as a friend function with chaining

private:
	//Data
	string current_string; // private string variable
};