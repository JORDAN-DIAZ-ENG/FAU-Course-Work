/******************************************************************************	S	A M P L E	T E S T	D R I V E R

Remember to always comment.	Documentation is very important!

*****************************************************************************/
//*****************************************************************************
//P R O G R A M	H E A D E R
//
//	Name: Jordan Diaz
//	Z#:	Z23554771
//	Instructor:	Dr. Bullard
//	Class:	Data Structures
//	Term:	Spring 2021
//	Assignment #7 (vlist)
//	Due Date:	March 22, 2021
//	Due Time:	11:59PM
//	Points:	100
//
//	Description: This program accesses your C++language skills.
//	After completing this assignment you will be able to perform the following:
//
//	(1) Manage a vector(allocatm and de-allocate memory, insert inorder, remove, etc).
//	(2) Implement a default constructor and a copy constructor.
//	(3) Implement an insert function to add a string, in order, into a vector
//	(4) Implement a remove function to delete a string from a vector
//******************************************************************************

#include <iostream>
#include <string>
#include "vlist.h" 
using namespace std;

int main()
{

	//Testing default constructor
	cout << "***********************************************************" << endl;
	cout << "Test1:Testing the default constructor for string\n"; 
	vlist String_List;
	cout << endl << endl;
	cout << "*****************End of Test1******************************" << endl;
	
	//Testing functionality for string list 
	cout << "***********************************************************" << endl;
	cout << "Test2: Testing Insert \n"; 
	String_List.insert("Hello"); 
	String_List.insert("Zebra"); 
	String_List.insert("Good_Bye"); 
	String_List.insert("Space"); 
	String_List.insert("No_One"); 
	String_List.print();
	cout << "*****************End of Test2******************************" << endl;
	
	cout << endl << endl;
	cout << "***********************************************************" << endl;
	cout << "Test 3: Testing copy constructor for string \n"; 
	vlist Copied_String = String_List; 
	Copied_String.print();
	String_List.print();
	cout << "*****************End of Test3******************************" << endl;

	cout << endl << endl;
	cout << "***********************************************************" << endl;
	cout << "Test 4: Testing Remove for string \n"; 
	cout << "Testing Search and IsEmpty also\n"; 
	String_List.remove("Zebra"); 
	String_List.remove("Good_Bye"); 
	String_List.remove("Hello"); 
	String_List.remove("No_One"); 
	String_List.remove("Space"); 
	String_List.remove("Hello");

	if (String_List.isEmpty())
	{
		cout << "String_List is Empty!"<<endl;
	}
	else
	{
		cout << "String_List is NOT Empty!" << endl;
	}
	cout << "*****************End of Test4******************************" << endl;
	cout << endl << endl;
	cout << "When leave main destructor will be called" << endl;

	return 0;
}
