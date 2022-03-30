
#include "state.h"
#include <iomanip>  //need to use formatting manipulators


/***********************FUNCTION HEADER ******************************************************************************************************************
Name:  Default Constructor
Pre-Conditon: The count, capacity, and the dynamic array (pop_DB) have not been initialized.
Post-Condition: The count, capacity, and the dynaic array (pop_DB) have been initialized.
Description:  The function initiailizes the state (private data) of the class state_class. It reads the data stored in the datafile "census2020_data.txt"
			  into the dynamic array, pop_DB.  Initially, count is set to 0, capacity to 5, and pop_DB is allocated 5 cells.  If pop_DB become full,
			  double_size is called, which doubles the capacity of pop_DB.

**********************************************************************************************************************************************************/
state_class::state_class()
{
	//intially count, capacity, and pop_DB are initialized with the following values:
	cout << "default constructor has been invoked \n";
	count = 0;
	capacity = 5;
	pop_DB = new population_record[capacity]; // initialization of the dynamic array

	string line;					// The current line being read
	string nameOfState = ""; 
	string digitText = "";			
	ifstream infile("census2020_data.txt");
	int space_location = 0;

	if (infile.is_open()) { cout << "file opened successfully\n"; }

	while (!infile.eof())
	{
		if (Is_Full())
		{
			double_size();
		}

		getline(infile, line);

		for (int i = line.length() - 1; i >= 0; i--) // Looks through every character in the line
		{
			if (line[i] == ' ')
			{
				space_location = i;
				break;
			}
		}	

		pop_DB[count].population = stod(line.substr(space_location + 1, line.length() - space_location - 1));
		pop_DB[count].state_name = line.substr(0, space_location);

		count++;
		space_location = 0;
	
	}
	infile.close();
	cout << "end of file reached\n";
}

/******************************************************************************************************************************************************
Name:	Copy Constructor
Pre-Condition: the count, capacity, pop_DB are not yet initialized
Post-Condition the count, capacity, pop_DB are initialized using the original object
Description: Copy constructor, a member function that initializes an object using another object of the same class..
******************************************************************************************************************************************************/
state_class::state_class(const state_class &org)
{
	// org stands for original
	count = org.count;
	capacity = org.capacity;
	pop_DB = new population_record[capacity];

	for (int i = 0; i < count; i++)
	{
		pop_DB[i] = org.pop_DB[i];
	}
}

/******************************************************************************************************************************************************
Name: Destructor
Pre-Condition: memory has not been de-allocated
Post-Condition memory has been de-allocated automatically at the end of the program
Description: destructor which de-allocates all memory allocated to the dynamic pop_DB using the new funciton.
******************************************************************************************************************************************************/
state_class::~state_class()
{
	cout << "destructor is called\n";
	delete[] pop_DB;
}

/******************************************************************************************************************************************************
Name: double_size	Mutator
Pre-Condition	the capacity(size) has not been doubled
Post-Condition	the capacity(size) has been doubled
Description:	double the capacity(size) of the memory allocate to the dynamic array pop_DB.
******************************************************************************************************************************************************/
void state_class::double_size()
{
	capacity = capacity * 2;
	population_record* temp = new population_record[capacity];
	
	for (int i = 0; i < count; i++)
	{
		temp[i] = pop_DB[i];
	}

	delete[] pop_DB;
	pop_DB = temp;

	cout << "size doubled\n";
}

/******************************************************************************************************************************************************
Name:	overload operator+
Pre-Condition r population record is not inserted into the dynamic array 
Post-Condition r population record is inserted into the dynamic array
Description:overload operator+ without chaining.  The function inserts a popultation record into the population dynamic array (pop_DB).
******************************************************************************************************************************************************/
void state_class::operator+(const population_record& r)
{
	//Testing operator+, Is_Full, double_size, and Print_ALL
	if (Is_Full())
	{
		double_size();
	}

	if (!Is_Full())
	{
		pop_DB[count] = r;
		count++;
	}
}

/******************************************************************************************************************************************************
Name: search	Accessor
Pre-Condition Has not looked through the pop_DB for a specific state
Post-Condition looked through pop_DB for a state name that matches the state thats being looked for and returns the index, otherwise return -1
Description:search pop_DB for a state in pop_DB. If the state is in pop_DB the location of the record is return; otherwise a -1 is returned.
******************************************************************************************************************************************************/
int state_class::Search(const string& state)
{
	cout << "Searching state for\n";
	// get the value in which the name of the state matches the one being looked for
	for (int i = 0; i < count; i++)
	{
		if (pop_DB[i].state_name == state)
		{
			cout << "state is: " << pop_DB[i].state_name << endl;
			return i; 
		}
	}
	return -1;
}


/******************************************************************************************************************************************************
Name: Mutator
Pre-Condition	has not removed a specific state from pop_DB
Post-Condition has removed a state from pop_DB with its data
Description:deletes a population record from pop_DB if the key field matches the state name.
******************************************************************************************************************************************************/
void state_class::Remove(const string& state)
{
	int i = Search(state);
	if (i != -1)
	{
			for (int j = i; j < count - 1; j++)
			{
				pop_DB[j] = pop_DB[j + 1];
			}
			if (!Is_Empty())
			{
				count--;
			}	
	}
}


/******************************************************************************************************************************************************
Name: Print_ALL_To_File
Pre-Condition The contents of pop_DB have not been printed to a file
Post-Condition The contents of pop_DB has been printed to a file with formatting 
Description: prints all the fields of all the population records stored in pop_DB to the filename stored in datafile.
******************************************************************************************************************************************************/
void state_class::Print_ALL_To_File(const string& filename)
{
	ofstream outfile;

	outfile.open(filename);

	for (int i = 0; i < count; i++)
	{
		outfile << fixed << setprecision(0) << setw(20);
		outfile << pop_DB[i].state_name << " " << pop_DB[i].population << endl;
	}

	outfile.close();
	
	//place your code here
}
/******************************************************************************************************************************************************
Name: Print All
Pre-Condition nothing has been printed yet from pop_DB
Post-Condition prints all fields of stored in pop_DB to the screen with formatting
Description: prints all the fields of all the population records stored in pop_DB to the screen.
******************************************************************************************************************************************************/
void state_class::Print_ALL()
{
	cout << "\tState Name Population\n";
	for (int i = 0; i < count; i++)
	{
		cout << fixed << setprecision(0) << setw(20);
		cout << pop_DB[i].state_name << " " << pop_DB[i].population << endl;
	}
}


/******************************************************************************************************************************************************
Name: Print Range
Pre-Condition has not yet print anything to the screen
Post-Condition prints the state name and population between the min and max, inclusive, and formats them
Description: prints all the fields of all the population records stored in pop_DB with a population between min and max to the screen;
******************************************************************************************************************************************************/
void state_class::Print_Range(const int min, const int max)
{
	for (int i = 0; i < count; i++)
	{
		if (pop_DB[i].population >= min && pop_DB[i].population <= max)
		{
			cout << fixed << setprecision(0) << setw(20);
			cout << pop_DB[i].state_name << " " << pop_DB[i].population << endl;
		}
	}
}


/******************************************************************************************************************************************************
Name: Accessor
Pre-Condition The number of states has not been counted 
Post-Condition The number of states with a population between min and max, inclusive, are counted and stored in a variable and returned 
Description: returns the total number of states with a population between min and max, inclusive.
******************************************************************************************************************************************************/
int state_class::State_Count(const int min, const int max)
{
	int statesCounted = 0;
	for (int i = 0; i < count; i++)
	{
		if (pop_DB[i].population >= min && pop_DB[i].population <= max)
		{
			statesCounted++;
		}
	}
	if (statesCounted > 0) { return statesCounted; }

	return 0;
}

/******************************************************************************************************************************************************
Name: Mutator
Pre-Condition: indexes in the array are not sorted by the alphabetical value of the string
Post-Condition: indexes in the array are sorted by the alphabetical value of the string
Description: sorts the array pop_DB in alphabetical order based on state_name field using insertion sort algorithm
******************************************************************************************************************************************************/
void state_class::Sort()
{
	population_record temp;

	for (int i = 1; i < count; i++)
	{
		temp = pop_DB[i];
		int j = i - 1;
		while ((j >= 0) && (pop_DB[j].state_name > temp.state_name))
		{
			pop_DB[j + 1] = pop_DB[j];
			j--;
		}
		pop_DB[j + 1] = temp;
	}
}
