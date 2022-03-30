#include <iostream>
#include <string>
#include "stack.h"
using namespace std;

/********************************************************************************************

Name:	Jordan Diaz		Z#:	Z23554771
Course: Data Structures and Algorithm Analysis (COP3530) Professor: Dr. Lofton Bullard
Due Date:	2/26/2021	Due Time:	11:59pm
Total Points: 25 Assignment 5: stack assignment with postfix

Description: this program converts a postfix expression to infix
*********************************************************************************************/
int main() //Driver
{
	//Initialize
	stack S, D;
	string  userPostfixExpression;
	char userInput = 'n';

	do
	{
		//Initial Question
		userPostfixExpression = "";
		cout << "Enter an expression in postfix notation: ";
		getline(cin, userPostfixExpression); //gets the whole line, if you just use cin >> userInput, it would stop whenever there is a space

		if (S.isValid(userPostfixExpression))
		{
			//Calculation and output
			S.Convert(userPostfixExpression); //convert users expression
			S.print(); //print users expression
			S.~stack(); //delete the stack 
		}

		//Ask for continuation
		cout << "Enter another postfix expression: Y or N? ";
		cin >> userInput;
		cin.ignore();

	} while (userInput == 'Y' || userInput == 'y');

	return 0;
}