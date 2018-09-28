#include "Encounter.h"

Encounter::Encounter() {
	int numUnits = 0;
	int index = 0;
}

/*
Builds an encounter list from reading in units from a saved file
*/
Encounter::Encounter(std::string filename) {
	index = 0;
	std::ifstream fin(filename);
	if (fin.is_open())
	{
		char * line = new char;

		fin.getline(line, 256);
		std::string lineString = line;
		setNumUnits(atoi(line));

		while (!fin.eof())
		{
			fin.getline(line, 256);
			std::string lineString = line;
			lineString.append(",1"); //Denotes favorite == true
			list.push_back(Unit(lineString));
		}

	}
	else {
		std::cout << "Error opening " << filename << ". Saved data failed to retrieve." << std::endl;
	}
	fin.close();
	update();
}

/*
Outputs favorited units to the save file in proper format, overwriting whats there.
*/
void Encounter::save(std::string filename) {
	std::ofstream fout(filename);
	if (fout.is_open())
	{
		//Get the number of favorite units, and output that number to the file
		int numFavoriteUnits = 0;
		for (int i = 0; i < getNumUnits(); i++) {
			if (getUnit(i).isFavorite()) numFavoriteUnits++;
		}
		fout << numFavoriteUnits << std::endl;

		//Output the favorite units themselves to the file
		for (int i = 0; i < getNumUnits(); i++) {
			if (getUnit(i).isFavorite()) {
				fout << getUnit(i).getName() << "," << getUnit(i).getInitiative() << "," <<
					    getUnit(i).getHP() << "," << getUnit(i).getNote() << std::endl;
			}
		}
	}
	else {
		std::cout << "Error opening " << filename << ". Failed to write save data to file." << std::endl;
	}
	fout.close();
}

/*
Sorts the list, and removes dead, non-favorited units
TODO: check this for bugs; specifically I'm worried that removing a bunch of dead units will mess up the index if they are removed on their turn.
Especially because the list is sorted based on this index immediately afterward.
*/
void Encounter::update() {
	//Remove dead units
	for (int i = 0; i < getNumUnits(); i++) {
		if (!getUnit(i).isFavorite() && getUnit(i).getHP()<=0 && AUTO_REMOVE_DEAD_UNITS) {
			list.erase(list.begin() + i);
		}
	}
	//Sort the list in descending order
	std::string temp = getUnit(getIndex()).getName();
	std::sort(list.begin(), list.end());
	setIndex(getUnitIndex(temp));
}

void Encounter::addUnit(std::string unitString) {
	list.push_back(Unit(unitString));
	update();
}

/*
Searches for a given name and removes it from the list
*/
void Encounter::deleteUnit(std::string name) {
	int deletionIndex = getUnitIndex(name);
	if (deletionIndex >= 0) {
		list.erase(list.begin() + deletionIndex);
	} else{
		std::cout << "Error: Cannot find unit for deletion." << std::endl;
	}
	update();
}

/*
Searches for a given name and returns its index; returns -1 if not found.
*/
int Encounter::getUnitIndex(std::string name) {
	for (int i = 0; i < getNumUnits(); i++) {
		if (name == getUnit(i).getName()) {
			return i;
		}
	}
	return -1;
}

/*
Clears all non-favorited units from the list
*/
void Encounter::clear() {
	for (int i = 0; i < getNumUnits(); i++) {
		if (!getUnit(i).isFavorite()) {
			list.erase(list.begin() + i);
		}
	}
	update();
}

/*
Edits a unit's data, returns the old unit
*/
Unit Encounter::edit() {

	update();
}

std::string Encounter::toString() {
	std::stringstream ss;
	ss << std::setw(OUTPUT_WIDTH) << "NAME" << "INITIATIVE" << "HP" << "NOTE" << std::endl;
	for (int i = 0; i < getNumUnits(); i++) {
		if (i == getIndex()) ss << std::setw(OUTPUT_WIDTH) << ">";
		else ss << std::setw(OUTPUT_WIDTH) << "-";

		ss << getUnit(i).toString() << std::endl;
	}
	ss << std::endl;
	return ss.str();
}

void Encounter::print() {
	std::cout << toString() << std::endl;
}

int Encounter::setNumUnits(int newNumUnits) {
	int temp = numUnits;
	this->numUnits = newNumUnits;
	return temp;
}

int Encounter::setIndex(int newIndex) {
	int temp = index;
	this->index = newIndex;
	return temp;
}