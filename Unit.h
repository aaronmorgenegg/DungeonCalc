#pragma once

#include "Utils.cpp"


/*
Unit class that details a single unit and its stats in an encounter list.
*/
class Unit {
public:
	Unit();
	Unit(std::string name, int initiative, int hp, std::string note, bool favorite);
	Unit(std::string unitString);
	bool operator < (const Unit& str) const;
	std::string toString();
	std::string setName(int newName);
	int setInitiative(int newInitiative);
	int setHP(int newHP);
	std::string setNote(std::string newNote);
	bool setFavorite(bool newFavorite);
	std::string getName() { return name; }
	int getInitiative() { return initiative; }
	int getHP() { return hp; }
	std::string getNote() { return note; }
	bool isFavorite() { return favorite; }
private:
	std::string name;
	int initiative;
	int hp;
	std::string note;
	bool favorite;
};