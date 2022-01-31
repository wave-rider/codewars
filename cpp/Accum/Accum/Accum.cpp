// Accum.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
#include <cctype>

class Accumul
{
public:
    static std::string accum(const std::string& s);
};

std::string Accumul::accum(const std::string& s) {
    auto it = s.cbegin();
    std::string result;
    if (s.length() == 0) {
        return result;
    }

    result += toupper(s[0]);
    it++;
    int index = 1;

    for (; it != s.cend(); ++it) {
        index++;
        result += '-';
        result += toupper(*it);
        char low_char = tolower(*it);
        result += string(index, low_char);
        /*for (int i = 1; i < index; i++)
        {
            result += low_char;
        }*/
    }
    return result;
}

int main()
{
    std::cout << "Hello World!\n";
    std::cout << Accumul::accum("zpglnrxqenu");
}



//
//write function accum :
//
//Examples:
//accum("abcd") -> "A-Bb-Ccc-Dddd"
//accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
//accum("cwAt") -> "C-Ww-Aaa-Tttt"
//The parameter of accum is a string which includes only letters from a..z and A..Z.