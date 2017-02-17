/*
Dungeons and Dragons calculator, useful for a few things when DMing.
Written by Aaron Morgenegg

Version 1.0 - 8/13/2016 - Original Release
Version 1.0.1 - 8/25/2016 - Added note feature for units in the initiative tracker

Program Functions:
	Has basic functionality like a help menu and quit.
	Has a very basic 4 function calculator, can calculate a single operation per line
	When given a number, generates a random number from 1 to that number.
	If given a dice roll, rolls that dice. ie 2d8+2.
	Can keep track of initiative, and can keep notes for each character

Ideas for future versions:
	Allow for saving/loading of initiative list
	Further foolproof the input so the program doesn't outright crash because of user error
	Add a counter for each unit, that can be set at an initial value, and then counts down every time it is their turn again. Also make a message appear each time it counts down, or a custom message when it ends.
*/

#include <iostream>
#include <time.h>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

//Initiative Class - has a name and an initiative associated with it.
struct unit {
public:
	unit() {
		this->name = "";
		this->initiative = 0;
		this->note = "";
	}
	unit(string name, int initiative) {
		this->name = name;
		this->initiative = initiative;
		this->note = "";
	}
	unit(string name, int initiative, string note) {
		this->name = name;
		this->initiative = initiative;
		this->note = note;
	}
	bool operator < (const unit& str) const
	{
		return (initiative > str.initiative);
	}
	string setName(int newName) {
		string temp = name;
		this->initiative = newName;
		return temp;
	}
	int setInitiative(int newInitiative) {
		int temp = initiative;
		this->initiative = newInitiative;
		return temp;
	}
	string setNote(string newNote) {
		string temp = note;
		this->note = newNote;
		return temp;
	}
	string getName() {
		return name;
	}
	int getInitiative() {
		return initiative;
	}
	string getNote() {
		return note;
	}
private:
	string name;
	int initiative;
	string note;
};

//checks if a string is an integer or not. Return true if it is, false if it is not. Pulled shamelessly from stack overflow
bool isStringInteger(const string &s) {
		return !s.empty() && find_if(s.begin(),
		s.end(), [](char c) { return !isdigit(c); }) == s.end();
}

//Display the help menu
void help() {
	cout << "Dungeon calc is a command line based program. Type your commands after the '#' symbol. Commands can be shortened to just the first letter and still be valid." << endl;
	cout<< "Valid commands include:" << endl;
	cout << "BASIC COMMANDS AND DICE ROLLS:" << endl;
	cout << "	help - displays this help menu" << endl;
	cout << "	quit - exits the program" << endl;
	cout << "	2+2 - adds the two numbers" << endl;
	cout << "	2-2 - subtracts the two numbers" << endl;
	cout << "	2*2 - multiplies the two numbers" << endl;
	cout << "	2/2 - divides the two numbers" << endl;
	cout << "	1d4 - rolls specified dice. Any positive numbers can be used, such as 2d8(rolls 2 8 sided dice), or 30d10(rolls 30 10 sided dice)." << endl;
	cout << "	1d4+2 - A value can also be added or subtracted from a dice roll automatically, for example 2d8-2 subtracts a 2 to the end of the dice roll." << endl;
	cout << "	20 - Typing a single number into the command line will generate a random value from 1 to that number." << endl;
	cout << "INITIATIVE:" << endl;
	cout << "	add herbert 17 - adds the given name and initiative to the combat list. A dice roll can be used instead of a number for the initiative." << endl;
	cout << "	delete herbert - deletes the given name from the initative list. Bye bye herbert!" << endl;
	cout << "	clear - clears the entire combat list." << endl;
	cout << "	next - rotates to the next units turn on the list." << endl;
	cout << "	edit herbert 9001 - edits the initiative of the specified creature to the given value." << endl;
	cout << "	print - prints out the entire combat list, with () around whose turn it is currently." << endl;
}

//returns the result of a dice roll, given a line of input in the form of 1d6 or 10d20+6
int rollDice(string input) {
	int fPos=0;
	int modifier=0;
	int numDice=0;
	int sizeDice=0;
	int retVal=0;
	int dPos = input.find_first_of('d'); //position of the 'd' in 10d6, for example
	int mPos = input.find_first_of('-'); //position of the '-' in 10d6-2, for example
	int aPos = input.find_first_of('+'); //position of the '+' in 10d6+2, for example
	//Pull out the number of dice at the front of the input
	numDice = stoi(input.substr(0, dPos));
	//Determine where the math is, if it exists.
	if (mPos >= 0) {
		fPos = mPos;
		modifier = -1*stoi(input.substr(mPos + 1, input.size()));
	}
	else if (aPos >= 0) {
		fPos = aPos;
		modifier = stoi(input.substr(aPos + 1, input.size()));
	}
	else {
		fPos = input.size() + 1;
		modifier = 0;
	}
	//get the size of the dice
	sizeDice = stoi(input.substr(dPos+1, fPos));
	//Get the math done son
	for (int i = 0; i < numDice; i++) {
		retVal += rand() % sizeDice + 1;
	}
	return retVal+modifier;
}

//Gets a random number from 1 to that number. Returns 0 if an invalid number is given(ie less than 1).
int getRandomNumber(int num) {
	if (num <= 0) {
		return 0;
	}
	else {
		return rand() % num + 1;
	}
}

//Recieves a string in the form of addition(2+2) and returns the completed equation
double add(string input) {
	double firstOperand = stod(input.substr(0, input.find('+', 0)));
	double secondOperand = stod(input.substr((input.find('+', 0) + 1), string::npos));
	return firstOperand + secondOperand;
}

//Recieves a string in the form of subtraction(2-2) and returns the completed equation
//this is a bit more complicated because of the possibility of extra negative signs
double subtract(string input) {
	bool firstNeg=false;
	if (input[0] == '-') {
		input.erase(0, 1);
		firstNeg = true;
	}
	double firstOperand = stod(input.substr(0, input.find('-', 0)));
	double secondOperand = stod(input.substr((input.find('-', 0) + 1), string::npos));
	if (firstNeg) {
		return (-1 * firstOperand) - secondOperand;
	}
	return firstOperand - secondOperand;
}

//Recieves a string in the form of multiplication(2*2) and returns the completed equation
double multiply(string input) {
	double firstOperand = stod(input.substr(0, input.find('*', 0)));
	double secondOperand = stod(input.substr((input.find('*', 0) + 1), string::npos));
	return firstOperand * secondOperand;
}

//Recieves a string in the form of division(2/2) and returns the completed equation
double divide(string input) {
	double firstOperand = stod(input.substr(0, input.find('/', 0)));
	double secondOperand = stod(input.substr((input.find('/', 0) + 1), string::npos));
	return firstOperand / secondOperand;
}

//Processes the string to either a random number, a die roll, or a math equation
double process(string input) {
	//If its a die roll, roll that dice
	if (input.find_first_of('d') != string::npos) {
		return rollDice(input);
	}
	//if it is multiplication, do the math
	else if (input.find_first_of('*') != string::npos) {
		return multiply(input);
	}
	//if it is division, do the math
	else if (input.find_first_of('/') != string::npos) {
		return divide(input);
	}
	//if it is addition, do the math
	else if (input.find_first_of('+') != string::npos) {
		return add(input);
	}
	//if it is subtraction, do the math
	//Putting this after the other operations makes negative numbers work nice lol.
	else if (input.find_first_of('-') != string::npos) {
		return subtract(input);
	}
	//if it is just a number, get a random number from 1 to that number.
	else if (isStringInteger(input)) {
		return getRandomNumber(stoi(input));
	}
	//Otherwise, it is invalid. DISQUALIFIED!
	else{
		cout << "ERROR: Invalid input. Type 'help' for a list of valid inputs." << endl;
		return NULL;
	}
}

//prints the whole list
void printList(vector<unit> encounter, int encounterIndex) {
	int count = 0;
	for (vector<unit>::iterator i = encounter.begin(); i != encounter.end(); ++i) {
		if (encounterIndex - 1 == count) {
			cout << "(" << encounter[count].getInitiative() << ") " << encounter[count].getName() << " " << encounter[count].getNote() << endl;
		}
		else {
			cout << encounter[count].getInitiative() << " " << encounter[count].getName() << encounter[count].getNote() << endl;
		}
		count++;
	}
}

//searches list for given name, returns position of name or -1 if it isn't found
int findName(vector<unit> encounter, string target) {
	int pos = 0;
	while (!encounter.empty()) {
		if (encounter[pos].getName() == target) {
			return pos;
		} else{
			pos++;
		}
	}
	return -1;
}

//sorts the list by initiative
void sortList(vector<unit> &encounter, int &encounterIndex) {
	string temp = encounter[encounterIndex].getName();
	sort(encounter.begin(), encounter.end());
	encounterIndex = findName(encounter, temp);
}

//find and delete a given name in the vector. Return the unit just in case its needed
unit deleteEntry(vector<unit> &encounter, string target) {
	int pos = findName(encounter, target);
	unit temp;
	if (pos == -1) {
		cout << "ERROR: Name not found" << endl;
	}
	else {
		temp = encounter[pos];
		encounter.erase(encounter.begin() + pos);
	}
	return temp;
}

//given a unit, add a new entry with the given stats
void addEntry(vector<unit>& encounter, unit target,int encounterIndex) {
	encounter.push_back(target);
	sortList(encounter,encounterIndex);
}

//given a string including a name, a space, and then the new initiative, find the given name and replace its initiative with new initiative.
void editEntry(vector<unit> &encounter, string name, int newInitiative) {
	int pos = findName(encounter, name);
	if (pos == -1) {
		cout << "ERROR: Name not found" << endl;
	}
	else {
		encounter[pos].setInitiative(newInitiative);
	}
}

//given a string including a name, a space, and then the new note, find the given name and replace its initiative with new initiative.
void editEntry(vector<unit> &encounter, string name, string newNote) {
	int pos = findName(encounter, name);
	if (pos == -1) {
		cout << "ERROR: Name not found" << endl;
	}
	else {
		encounter[pos].setNote(newNote);
	}
}

int main() {
	//Seed the random number
	srand(time(NULL));
	//Set up the initiative vector
	vector<unit> encounter;
	encounter.shrink_to_fit();
	int encounterIndex = 0;
	//Starting Message
	cout << "Welcome to dungeon calc 1.0.1. Enter commands following the #. Type 'help' for a list of commands." << endl;
	//Function loop - Get input and process input into useful stuff.
	bool end = false;
	while (!end) {
		cout << '#';
		string input;
		getline(cin, input);
		//If it starts with a letter it is some kind of command. Process the command.
		if (input[0] >= 'a' && input[0] <= 'z' || input[0] >= 'A' && input[0] <= 'Z') {
			//Quit program if they type quit.
			if(input[0]=='q' || input[0]=='Q'){
				end=true;
			}
			//Help menu
			else if (input[0] == 'h' || input[0] == 'H') {
				help();
			}
			//clear initiative list, empty the vector
			else if (input[0] == 'c' || input[0] == 'C') {
				encounterIndex = 0;
				encounter.clear();
				encounter.shrink_to_fit();
			}
			//delete a specified entry from list
			else if (input[0] == 'd' || input[0] == 'D') {
				string name = input.substr(input.find(' ', 0) + 1, string::npos);
				deleteEntry(encounter, name);
			}
			//add a new entry to list, and sort the list
			else if (input[0] == 'a' || input[0] == 'A') {
				//use some ugly string manipulation to get the name and initiative
				string target = input.substr(input.find(' ', 0) + 1, string::npos);
				string name = target.substr(0, target.find(' ', 0));
				string temp = target.substr(target.find(' ', 0) + 1, string::npos);
				int initiative = 0;
				if (isStringInteger(temp)) {
					initiative = stoi(temp);
				} else{
					initiative = process(temp);
				}
				unit newUnit = unit(name, initiative);
				addEntry(encounter, newUnit, encounterIndex);
			}
			//next functionality. Display current entry, then rotate to next entry
			else if (input[0] == 'n' || input[0] == 'N') {
				if (encounterIndex >= encounter.size()) {
					encounterIndex = 0;
				}
				cout << encounter[encounterIndex].getName() << " " << encounter[encounterIndex].getInitiative() << " " << encounter[encounterIndex].getNote() << endl;
				encounterIndex++;
			}
			//edit specified entry in list
			else if (input[0] == 'e' || input[0] == 'E') {
				//more ugly string manipulation to get what we need
				string target = input.substr(input.find(' ', 0) + 1,string::npos);
				string name = target.substr(0, target.find(' ', 0));
				string temp = target.substr(target.find(' ', 0) + 1, string::npos);
				int newInitiative = 0;
				if (isStringInteger(temp)) {
					newInitiative = stoi(temp);
					editEntry(encounter, name, newInitiative);
				}else {
					editEntry(encounter, name, temp);
				}
				sortList(encounter,encounterIndex);
			}
			//print whole list
			else if (input[0] == 'p' || input[0] == 'P') {
				printList(encounter,encounterIndex);
			}
			else {
				cout << "Invalid input. Type 'help' for a list of valid inputs." << endl;
			}
		}
		//Otherwise it is an equation of some sort. Math, Die rolls, or Random Numbers are easily handled by this fancy function
		else {
			cout<<process(input)<<endl;
		}
	}
}
