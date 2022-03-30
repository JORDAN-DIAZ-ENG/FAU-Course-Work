#include <iostream>
#include <string>
#include "sentence.h"
using namespace std;

//*************************************************************************************
//Name:	sentence
//Precondition: nothing has been initialized
//Postcondition: initialized front and back
//Description: default constructor
//*************************************************************************************
sentence::sentence()
{
    front = back = 0;
}

//*************************************************************************************
//Name:	sentence(const string& s)
//Precondition: 
//Postcondition: 
//Description: Explicit value constructor initializes state variables and nodes with desired values
//*************************************************************************************
sentence::sentence(const string& s)
{
    //Initialize
    front = back = 0;
    int len = s.length();

    //If the string is empty
    if (len == 0)
    {
        front = 0;
        return;
    }

    //Initialize strings
    string current, space;
    space = " ";

    //start from 0 and end at the end of the string
    for (int i = 0; i < len; i++)
    {
        //if the current character in the string is not a space
        if (s[i] != ' ')
        {
            current += s[i]; //add the current character to the string
        }

        //if the current character in the string is a space
        if (s[i] == ' ')
        {
            add_back(current); //add the current node to the back of the sentence
            add_back(space); //add the current node to the back of the sentence
            current = "";
        }

        //if the next character in the string is the null character
        if (s[i + 1] == '\0')
        {
            add_back(current); //add the current node to the back of the sentence
        }
    } 
}

//*************************************************************************************
//Name:	sentence(const sentence& org)
//Precondition: 
//Postcondition: 
//Description: copy constructor to be used during a call-by-value, return, or initialization/declaration of a sentence object
//*************************************************************************************
sentence::sentence(const sentence& org)
{
    //Initialize 
    front = back = 0;
    word* currentNode = org.front;

    //Do this until the last node
    while (currentNode != 0)
    {
        add_back(currentNode->term); //add the current node to the back of the sentence
        currentNode = currentNode->next; //move to the next node in the list
    }
}

//*************************************************************************************
//Name: ~sentence
//Precondition: 
//Postcondition: 
//Description: De-allocates all memory for a sentence
//*************************************************************************************
sentence::~sentence()
{
    cout << "Destructor has been called\n";

    //Initialize
    word* NodeToDelete = front;

    //Do this as long as the node to delete is not at the end of the list
    while (NodeToDelete != 0)
    {
        word* next = NodeToDelete->next; //create a copy of the next address
        delete NodeToDelete;
        NodeToDelete = next; //the value of the next node is saved by doing this
    }
    front = 0; // allows for multiple destructor calls
}

//*************************************************************************************
//Name:	length
//Precondition: 
//Postcondition: 
//Description: Determines the length of the sentence
//*************************************************************************************
int sentence::length()
{
    //Initialize
    int len = 0; // length
    word* nodeAddress = this->front;

    //if this is the last node
    if (nodeAddress == 0)
    {
        return len; //The length will be 0
    }
    else
    {
        //it is not the last node
        while (nodeAddress != 0)
        {
            len += nodeAddress->term.length(); //Adds the length of the string inside the node to the count
            nodeAddress = nodeAddress->next; //moves to the next node in the list
        }
        return len; 
    }
}

//*************************************************************************************
//Name: add_back
//Precondition: 
//Postcondition: 
//Description: Add a word (node) to the back of the sentence (the linked list)
//*************************************************************************************
void sentence::add_back(string& s)
{
    //If the first node is the last node (the only node)
    if (front == 0)
    {
        front = new word; //Allocate memory                                     
        front->term = s; //set the value of the data to the string input       
        front->next = 0; //set the next address to 0 (the end of the node)    
        back = front; //set back and front to 0, lets it be one node            
    }
    else
    {
        word* p = new word; //Allocate memory                               
        p->next = 0; //set the value of the next term to 0 (one node)          
        p->term = s; //set the node's data to the string input                  
        back->next = p; //set the next node to the beginning of the next word                                                     -
        back = p;                                                            
    }
}
//*************************************************************************************
//Name: operator<<
//Precondition: 
//Postcondition: 
//Description: Outputs sentence object and its nodes to output stream
//*************************************************************************************
ostream& operator<<(ostream& out, const sentence& A)
{
    //Initialize
    word* p; //current pointer, will point to the current node

    //start from the first node of the list, until the address = 0 (the last node), move to the next node
    for (p = A.front; p != 0; p = p->next)
    {
        out << p->term;  //Insert the value inside the current node
    }
    return out; //output the inserted data
}

//*************************************************************************************
//Name: operator=
//Precondition: 
//Postcondition: 
//Description: Assigns values of string to current setence object A
//*************************************************************************************
void sentence::operator=(const string& s)
{
    //Initialize
    front = back = 0;
    int len = s.length();

    //If the string is empty
    if (len == 0)
    {
        front = 0;
        return;
    }

    //Initialize strings
    string current, space;
    space = " ";

    //start from 0 and end at the end of the string
    for (int i = 0; i < len; i++)
    {
        //if the current character in the string is not a space
        if (s[i] != ' ')
        {
            current += s[i]; //add the current character to the string
        }

        //if the current character in the string is a space
        if (s[i] == ' ')
        {
            add_back(current); //add the current node to the back of the sentence
            add_back(space); //add the current node to the back of the sentence
            current = "";
        }

        //if the next character in the string is the null character
        if (s[i + 1] == '\0')
        {
            add_back(current); //add the current node to the back of the sentence
        }
    }
}

//*************************************************************************************
//Name: operator=
//Precondition: 
//Postcondition: 
//Description: Assigns values of string to current setence object A
//*************************************************************************************
sentence& sentence::operator=(const sentence& w)
{
    //Initialize
    front = 0;
    back = 0;
    word* A = w.front;

    //Do this until the end of the list
    while (A != 0)
    {
        add_back(A->term); //Add the data of A into the back
        A = A->next; // move to the next node in the list
    }

    return *this; //return the current object
}

void sentence::operator+(sentence& B)
{
    //Initialize
    word* combine = B.front;

    //if the front of B is not 0
    if (combine != 0)
    {
        //while not at the end of the list 
        while (combine != 0)
        {
            add_back(combine->term); //Add the term to the end of the list
            combine = combine->next; //move to the next node in the list 
        }
    }
    else
    {
        return;
    }
}

//*************************************************************************************
//Name: isEqual
//Precondition: 
//Postcondition: 
//Description: Returns true if two sentence objects are equal
//*************************************************************************************
bool sentence::isEqual(sentence& B)
{
    //if current length is not the same as the length of B(the sentence from the driver)
    if (length() != B.length())
    {
        return false; //The sentences are not equal
    }

    //Allocate memory
    word* p1 = new word;
    word* p2 = new word;

    //Initialize
    p1 = front;
    p2 = B.front;

    //Do this when both p1, and p2 are not at the end of the list
    while (p1 != 0 && p2 != 0)
    {
        //if the data in p1 does not match the data in p2
        if (p1->term != p2->term)
        {
            return false; //The sentences are not equal
        }

        p1 = p1->next;
        p2 = p2->next;
    }
    return true; //The sentences are equal
}

//*************************************************************************************
//Name: remove
//Precondition: 
//Postcondition: 
//Description: Deletes the first occurrence of string s in the current sentence object
//*************************************************************************************
word* sentence::search(const string& s)
{
    //Initialize
    word* p = front;

    //Do this until it reache the end
    while (p != 0)
    {
        //If the data in p is the same as the string input
        if (p->term == s)
        {
            return p; //address of data found
        }
		p = p->next; //move to the next 
    }
    return p; // not found
}


//*************************************************************************************
//Name: remove
//Precondition: 
//Postcondition: 
//Description: Deletes the first occurrence of string s in the current sentence object
//*************************************************************************************
void sentence::remove(const string& s)
{
    //Initialize
    word* p = search(s); // the searched node

    //if the current node is 0
    if (p == 0)
    {
        return;
    }
    else // current node is not 0
    {
        //if the current node is the last node
        if (p == front && front == back)
        {
            delete p; //delete the current node
            front = back = 0; // let it be one mode
        }
        else if (p == front) //if current node is the first node
        {
            front = front->next; //move to the next node
            delete p; //delete the current node
        }
        else
        {
            //Initialize
            word* back_ptr = front;

            //Do this as long as the back pointer is not at the end, and the next pointer to the back is not the searched node 
            while (back_ptr != 0 && back_ptr->next != p)
            {
                back_ptr = back_ptr->next; //move to the next node;
            }

            //If the searched node is at the end
            if (p == back)
            {
                back = back_ptr; //set back to the back pointer
            }

            back_ptr->next = p->next; //the back pointer's next is set to the searched pointer's next
            delete p; //delete the searched node
        }
    }
}