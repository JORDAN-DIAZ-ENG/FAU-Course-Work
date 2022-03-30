#include<iostream>
#include"bqueue.h"
using namespace std;

//*************************************************************************************
//Name:	bqueue (default constructor)
//Precondition: values have not been set
//Postcondition: front has been initialized to 0
//Description: initialize a default constructor
//*************************************************************************************
bqueue::bqueue()
{
	front = 0;
}

//*************************************************************************************
//Name:	~bqueue
//Precondition:	has not deleted nodes allocated by new 
//Postcondition: has deleted nodes allocated by new
//Description: deletes nodes allocated by new
//*************************************************************************************
bqueue::~bqueue()
{
	cout << "~QUEUE has been called\n";
	while (front != 0)
	{
		dequeue();
	}
}

//*************************************************************************************
//Name:	bqueue (copy constructor)
//Precondition: has not copied anything
//Postcondition: has copied the another instance of bqueue
//Description: copies an instance of bqueue
//*************************************************************************************
bqueue::bqueue(const bqueue& org)
{
	if (org.front == 0) //if the original queue is empty
	{
		cout << "The queue is empty, add items to the queue.\n";
	}
	else
	{
		//Initialize pointers
		bqnode* p1 = new bqnode;
		bqnode* p2 = new bqnode;

		//Copy the original
		front = p1;	//set the first pointer to the front of the queue
		front->priority = org.front->priority; //copy the data 

		bqnode* currentp = front;
		p2 = org.front->next;
		p1 = new bqnode;
		front->next = p1;

		while (p2 != org.front)
		{
			p1->priority = p2->priority; //copy the data
			p1->prev = currentp; //connect
			p1->next = new bqnode; //have next pointer be new node
			currentp = p1; //the current pointer is the next node
			p1 = p1->next; //move to the next node
			p2 = p2->next; //move to the next node
		}

		//make the nodes circular
		front->prev = currentp; //connect the front not to the back
		currentp->next = front; //connect the back node to the front
	}
}

//*************************************************************************************
//Name:	enqueue
//Precondition: node has not been added with data to the back of the queue
//Postcondition: node has been added with data to the back of the queue
//Description: Adds an element at the back of the queue
//*************************************************************************************
void bqueue::enqueue(int item)
{
	if (empty()) //node empty
	{
		front = new bqnode; //Creates a new node				   
		front->priority = item; //Assign the data to the node	  
		front->prev = front->next = front; //Make Circular	
	}
	else //non empty nodes
	{
		front->prev->next = new bqnode; //creates a new node at the back	
		front->prev->next->prev = front->prev; //sets the new node to back	
		front->prev = front->prev->next; //sets the back pointer to the new node
		front->prev->next = front; //sets the new node's next pointer to the front, now it's circular
		front->prev->priority = item; //Assign the data to the node	  
	}
}

//*************************************************************************************
//Name:	dequeue
//Precondition: node has not been removed from the front of the queue
//Postcondition: node has been removed from the front of the queue
//Description: remove the element at the front of the queue
//*************************************************************************************
void bqueue::dequeue()
{
	if (!empty())
	{	
		//if there is only one node
		if (front == front->prev)
		{
			bqnode* p = front; //set a pointer to the front
			front = 0; //change the location of front from the node that is going to be deleted
			delete p; //delete the node
		}
		else
		{
			bqnode* p1 = front; //set a pointer to the front
			front = front->next; //change the location of front to the next node
			front->prev = p1->prev; //let the previous pointer for the front be its old previous pointer
			front->prev->next = front; //The last node's next will be the front of the node
			delete p1; //delete the node
		}
	}
	else //node is empty
	{
		cout << "Cannot dequeue because the queue is empty\n";
	}
}

//*************************************************************************************
//Name: print
//Precondition: data has not been output to the screen
//Postcondition: data has been outupt to the screen
//Description: prints the data of each node onto the screen with formatting
//*************************************************************************************
void bqueue::print()
{
	if (empty()) //empty node
	{
		cout << "The Queue is empty, Information needs to be added\n";
	}
	else //node not empty
	{
		bqnode* p = front; //create a pointer that will go through each node starting at the front 
		cout << "[ ";
		do
		{
			cout << p->priority << " "; //print the data 
			p = p->next; //move to the next node
		} 
		while (p->next != front->next);
		cout << "]" << endl;
	}
}