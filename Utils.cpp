#include "Utils.h"

/*
Split a string with a delimitor character
Pulled from http://stackoverflow.com/questions/236129/split-a-string-in-c
*/
std::vector<std::string> split(const std::string &s, char delim) {
	std::vector<std::string> elems;
	split(s, delim, std::back_inserter(elems));
	return elems;
}