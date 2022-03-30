#pragma once

#include <iostream>
#include <string>
using namespace std;

typedef string stack_element;

class stack_node
{
public:
	stack_element data;
	stack_node* next;
};

class stack
{
public:
	stack() {/*cout<<"Inside Default Constructor\n"*/; s_top = 0; } //Default Constructor, Inline function
	~stack(); //Destructor
	stack(const stack&); //Copy constructor
	stack_element top(); //return string with the top element
	void pop(); //remove an element from the top of the stack
	void push(const stack_element&); //Add element to the top of the stack
	void print(); //display the data in the list
	void Convert(const stack_element&); //Converts postfix to infix
	bool isOperand(char x) { return (x >= 'a' && x <= 'z') || (x >= 'A' && x <= 'Z'); } //find if there is an operand or not
	bool isValid(const string& userInput); //checks if valid and supplies an error message

private:
	stack_node* s_top; //pointer address to the top of the stack
};