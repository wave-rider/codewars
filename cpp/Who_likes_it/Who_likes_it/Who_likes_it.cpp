// Who_likes_it.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>
#include <format>

std::string likes(const std::vector<std::string>& names)
{
    if (names.size() == 0) {
        return "no one likes this";
    }
    if (names.size() == 2) {
        return std::format("{0} likes this", names[0]);
    }
    return ""; // Do your magic!
}

int main()
{
    std::cout << "Hello World!\n";
}

/*
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
*/