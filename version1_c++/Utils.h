#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <time.h>
#include <algorithm>
#include <iterator>

const int OUTPUT_WIDTH = 20;
const bool AUTO_REMOVE_DEAD_UNITS = true;
const bool LOAD_SAVED_UNITS_ON_START = true;
const bool SAVE_FAVORITES_ON_CLOSE = true;
const std::string SAVE_FILENAME = "DungeonCalcSaveData.txt";

template<typename Out>
void split(const std::string &s, char delim, Out result);
std::vector<std::string> split(const std::string &s, char delim);