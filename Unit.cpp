#include "Unit.h"

Unit::Unit() {
	name = "";
	initiative = 0;
	hp = 0;
	note = "";
	favorite = false;
}

Unit::Unit(std::string name, int initiative, int hp, std::string note, bool favorite) {
	this->name = name;
	this->initiative = initiative;
	this->hp = hp;
	this->note = note;
	this->favorite = favorite;
}

/*
Comparison operator compares unit initiative in descending order
*/
bool Unit::operator < (const Unit& str) const
{
	return (this->initiative > str.initiative);
}

std::string Unit::toString() {
	std::stringstream ss;
	ss << std::setw(OUTPUT_WIDTH) << name << initiative << hp << note;
	return ss.str();
}

std::string Unit::setName(int newName) {
	std::string temp = name;
	this->initiative = newName;
	return temp;
}

int Unit::setInitiative(int newInitiative) {
	int temp = initiative;
	this->initiative = newInitiative;
	return temp;
}

int Unit::setHP(int newHP) {
	int temp = hp;
	this->hp = newHP;
	return temp;
}

std::string Unit::setNote(std::string newNote) {
	std::string temp = note;
	this->note = newNote;
	return temp;
}

bool Unit::setFavorite(bool newFavorite) {
	bool temp = favorite;
	this->favorite = newFavorite;
	return favorite;
}