#pragma once


class bqnode
{
public:
	int priority;
	bqnode* prev, * next;
};

class bqueue
{
public:
	bqueue();
	~bqueue();
	bqueue(const bqueue&);
	void enqueue(int);
	void dequeue();
	bool empty() { return front == 0; }
	void print();
private:
	bqnode* front; //use ONLY one pointer
};