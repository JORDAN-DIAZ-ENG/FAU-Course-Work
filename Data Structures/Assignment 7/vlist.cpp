#include <iostream>
#include <vector>
#include <string>
#include "vlist.h" using namespace std;

///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: vlist
//Precondition: Constructor has not been invoked.
//Postcondition: count = 0; vector size is 9.
//Description: Constructs an instance of a vlist object.
///////////////////////////////////////////////////////////////////////////////////////////////
vlist::vlist()
{
	cout << "Default Constructor Invoked";
	count = 0;
	DB.resize(9);
}

///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: vlist
//Precondition: A vlist object is being passed by reference.
//Postcondition: A hard copy of a vlist object has been created.
//Description: Creates a hard copy of a vlist object.
///////////////////////////////////////////////////////////////////////////////////////////////
vlist::vlist(const vlist & Org)
{
	cout << "Copy Constructor Invoked\n";

	DB = Org.DB;
	count = Org.count;
}

///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: ~vlist
//Precondition: Destructor has not been invoked.
//Postcondition: array DB deleted.
//Description: Deallocates memory of a vlist object.
///////////////////////////////////////////////////////////////////////////////////////////////
vlist::~vlist()
{
	cout << "Destructor Invoked" << endl;
	DB.clear();
	DB.shrink_to_fit();
}

///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: isEmpty
//Precondition: has not returned anything
//Postcondition: returned true or false based on if empty or not 
//Description: Checks if a vector is empty
///////////////////////////////////////////////////////////////////////////////////////////////
bool vlist::isEmpty() 
{
	if (DB.empty())
	{
		return true;
	}
	else
	{
		return false;
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: search
//Precondition: key has not been searched in the vector
//Postcondition: key has been searched and is either found or not found
//Description: look for a value based on a given key, returns the position if found, or the end if not
///////////////////////////////////////////////////////////////////////////////////////////////
vector<string>::iterator vlist::search(const string& key)
{
	for (vector<string>::iterator it = DB.begin(); it != DB.end(); it++)
	{
		if (*it == key)
		{
			cout << "Item Found\n" << *it << endl;
			return it;
		}
	}
	cout << "Item not found\n" << key << endl;
	return DB.end();
}


///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: insert
//Precondition: nothing has been inserted into the vector
//Postcondition: string has been inserted into the vector alphabetically
//Description: alphabetically inserts key into vector
///////////////////////////////////////////////////////////////////////////////////////////////
void vlist::insert(const string & key)
{
	//iterator starts at the beginning
	//stops at the end
	//increments by one
	for (vector<string>::iterator it = DB.begin(); it != DB.end(); it++) 
	{
		if (*it >= key) //if the value at the iterator is greater than or equal to key
		{
			DB.insert(it, key); //insert key at the location of the iterator 
			count++; //add to the count
			return; //stop running the function
		}
	}
	DB.insert(DB.end(), key); //if the end has been reached, add this to the end
	count++;

}

///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: remove
//Precondition: nothing has been removed from the vector
//Postcondition: if it exists, the key will be removed from the vector
//Description: removes a specific key from a vector
///////////////////////////////////////////////////////////////////////////////////////////////
void vlist::remove(const string& key)
{
	vector<string>::iterator it = search(key);

	if (it != DB.end())
	{
		DB.erase(it);
		count--;
	}
	else
	{
		cout << "Key was not found\n";
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////
//Function Name: print
//Precondition: nothing has been printed
//Postcondition: elements of a vector have been printed to the screen
//Description: prints the elements of a vector to the screen
///////////////////////////////////////////////////////////////////////////////////////////////
void vlist::print() 
{
	DB.shrink_to_fit();
	for (vector<string>::iterator it = DB.begin(); it != DB.end(); it++)
	{
		cout << *it << ' ';
	}
	cout << endl;
}