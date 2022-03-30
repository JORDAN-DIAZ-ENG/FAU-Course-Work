
#include <vector> 
#include <string>
using namespace std;

#ifndef vlist_H
#define vlist_H

class vlist
{
public:
	vlist(); // Constructs an instance of a vlist object.
	vlist(const vlist&); //Creates a hard copy of a vlist object.
	~vlist(); //destructor
	bool isEmpty(); //checks if vector is empty
	vector<string>::iterator search(const string&); //seach the vector for a specific key
	void insert(const string&); //add an item to a vector in order(alphabetical)
	void remove(const string&); //remove an item from vector
	void print(); //print every item stored in a vector
private:
	vector<string> DB;
	int count;
};

#endif