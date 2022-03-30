#include <iostream>
#include <string>
#include "stack.h"
using namespace std;


//*************************************************************************************
//Name:	~stack
//Precondition: elements in the stack have not been removed
//Postcondition: elements in the stack have been removed
//Description: destructor
//*************************************************************************************
stack::~stack()
{
	//Do this until the end of the stack
	while(s_top!=0)
	{
		pop(); //Remove the top element
	}
}

//*************************************************************************************
//Name:	pop
//Precondition: element at the top of the stack have not been removed
//Postcondition: element at the top of the stack have not been removed
//Description: Removes an element from the top of the stack
//*************************************************************************************
void stack::pop()
{
	//Initialize
	stack_node *p; //a pointer for assistance in the stack 
	
	//If the end of the stack
	if (s_top != 0)
	{
		p = s_top; //The temporary pointer is set to the value of the pointer pointing at the top of the stack
		s_top = s_top->next; //move the top to the next node, go down the stack
		delete p; //delete the temporary pointer with the value of the top of the stack
	}
}

//*************************************************************************************
//Name:	push
//Precondition: element has not been added to the stack 
//Postcondition: element has been added to the top of the stack
//Description: Adds an element to the top of the stack
//*************************************************************************************
void stack::push(const stack_element & item) 
{
	//Initialize and Allocate memory
	stack_node *p = new stack_node;

	p->data = item; //the data in p has been given the value from the function call (item)
	p->next = s_top; //link p to the top of the stack
	s_top = p; //set the top to p
}

//*************************************************************************************
//Name:	Convert
//Precondition: nothing has changed
//Postcondition: convert postfix to infix
//Description: converts a postfix expression to infix
//*************************************************************************************
void stack::Convert(const stack_element& ToChange) 
{
	//Initialize
	string op1, op2;
	stack_element changedString;

	//if the string to change is empty
	if (ToChange.length() == 0)
	{
		push(""); //push an empty string
		return; //stop running the function
	}

	//if the string to change has only one operand
	if (ToChange.length() == 1)
	{
		push("(" + ToChange + ")"); // add this to the stack
		return; //stop running the function
	}

	//Go through every character inside the stack_element to change
	for (int i = 0; i < ToChange.length(); i++)
	{
		//If the current character is in the alphabet
		if (isOperand(ToChange[i]))
		{
			string temp(1, ToChange[i]); //Turn the character into a string
			push(temp); //Add the character to the top of the stack
		}
		else if (ToChange[i] == '+' || ToChange[i] == '-' || ToChange[i] == '/' || ToChange[i] == '*') //if an operation
		{
			//Remove the elements 
			op2 = top(); //let the 2nd operand be the top of the stack
			pop(); //pull out the top element of the stack
			op1 = top(); //let the 1st operand be the top of the stack
			pop(); //pull out the top element of the stack

			//combine the elements into one string
			changedString = "("; 
			changedString += op1;
			changedString += " ";
			changedString.push_back(ToChange[i]);
			changedString += " ";
			changedString += op2;
			changedString.push_back(')');

			//add combined elements into one element into the stack
			push(changedString); //push string into the stack
		}
	}
}

//*************************************************************************************
//Name: isValid
//Precondition: true or false has not been returned 
//Postcondition: true of false has been returned
//Description: returns true or false based on if validity, shows error messages too
//*************************************************************************************
bool stack::isValid(const string& userInput)
{
	//Initialize
	int operands = 0, operations = 0;   

	//Go through each character in userInput
	for (int i = 0; i < userInput.length(); i++)
	{ 
		//count operands and operators
		if (isOperand(userInput[i])) { operands++; }
		else if (userInput[i] != ' ') { operations++; }
	}

	// if single operand expression
	if (userInput.length() == 1 && operands == 1) { return true; }

	//if empty string
	if (userInput.length() == 0) { return true; }

	//if there are more operators than operands
	if (operations >= operands)
	{ 
		cout << "Postfix expression invalid:\nToo many operators and not enough operands" << endl;
		return false;
	}
	else if (operands > 2 && operands >= operations * 2) //special case so cases like (a + b) do not fail
	{ 
		cout << "Postfix expression invalid:\nToo many operands and not enough operators" << endl;
		return false;
	}
	else if (operands > operations * 2) //if there are more operands than operators
	{ 
		cout << "Postfix expression invalid:\nToo many operands and not enough operators" << endl;
		return false;
	}

	return true;
}

//*************************************************************************************
//Name:	print
//Precondition: data has not been printed
//Postcondition: data has been printed
//Description: prints the data of the stack to the screen
//*************************************************************************************
void stack::print()
{
	//start from the top of a stack and work your way down until you hit 0 (the end of the stack)
	for(stack_node *p = s_top; p!=0; p=p->next)
	{
		cout<<p->data<<endl; //output the data in each
	}
}

//*************************************************************************************
//Name:	top
//Precondition: data from the top of the class has not been grabed
//Postcondition: data from the top of the class has been returned
//Description: grabs the data from the top of the stack
//*************************************************************************************
stack_element stack::top()
{
	//if the end of the stack
	if (s_top == 0)
	{
		exit(1); //exit the program
	}
	else
	{
		return s_top->data; //return the data from the top of the stack
	}
}

//*************************************************************************************
//Name:	stack (copy constructor)
//Precondition: copy of original stack has not been made
//Postcondition: copy of original stack has been made
//Description: copy a stack
//*************************************************************************************
stack::stack(const stack & Org)
{
	//Initialize
	(*this).s_top = 0; //The current object's top pointer is 0, start pointing from the top
	stack temp;	//temporary stack
	stack_node* p = Org.s_top; //become the pointer to the top of the original stack

	//Do this until the end of the stack is reached
	while(p!=0)
	{
		temp.push(p->data); //add the data from the original to the temporary
		p=p->next; //move down to the next element in the stack
	}

	p = temp.s_top; //starting point is from the top of the temporary stack

	//Do this until the end of the stack is reached
	while (p != 0)
	{
		(*this).push(p->data); //add the data from temp and add it to the current
		p = p->next; //move down to the next element in the stack
	}
}