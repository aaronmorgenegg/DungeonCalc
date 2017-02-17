#include "Encounter.h"

Encounter::Encounter() {
	int numUnits = 0;
	int index = 0;
}

/*
Builds an encounter list from reading in units from a saved file
*/
Encounter::Encounter(std::string filename) {

}

/*
Sorts the list, and removes dead, non-favorited units
*/
void Encounter::update() {

}

void Encounter::addUnit() {

}

void Encounter::deleteUnit() {

}

/*
Clears all non-favorited units from the list
*/
void Encounter::clear() {

}

/*
Edits a unit's data, returns the old unit
*/
Unit Encounter::edit() {

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