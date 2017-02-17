#pragma once

#include "Unit.cpp"

/*
A list of units, that can manage units and track initiative
*/
class Encounter {
public:
	Encounter();
	Encounter(std::string filename);
	void save(std::string filename);
	void update();
	void addUnit(std::string unitString);
	void deleteUnit(std::string name);
	int getUnitIndex(std::string name);
	void clear();
	Unit edit();
	std::string toString();
	void print();

	Unit getUnit(int index) { return list[index]; }
	int getNumUnits() { return numUnits; }
	int getIndex() { return index; }
	int setNumUnits(int newNumUnits);
	int setIndex(int newIndex);
	void incrIndex() { index++; }
	void decrIndex() { index--; }
private:
	std::vector<Unit> list;
	int numUnits;
	int index;
};