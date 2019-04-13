//
//  main.cpp
//  xandos
//
//  Created by wasabi on 8/04/19.
//  Copyright © 2019 wasabi. All rights reserved.
//

#include <iostream>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <chrono>
#include <unistd.h>
#include <algorithm>

using namespace std;

bool XO(std::string s)
{
    int x = 0;
    int o = 0;
    for (char &c : s)
    {
        char t = tolower(c);
        if (t=='x')
            x++;
        if (t=='o')
            o++;
    }
    return x==o;
    
}

bool XO1(const std::string& str)
{
    long xCount = std::count(str.begin(), str.end(), 'x') + std::count(str.begin(), str.end(), 'X');
    long oCount = std::count(str.begin(), str.end(), 'o') + std::count(str.begin(), str.end(), 'O');
    return xCount ==  oCount;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    auto start = chrono::steady_clock::now();
    //sleep(3);
    std::cout << XO1("A1ujSUqSbWvzgMGzowq33fEJjLceJ8PjLGL6AY34uivixJ9");
    auto end = chrono::steady_clock::now();
    cout << "Elapsed time in milliseconds : "
    << chrono::duration_cast<chrono::microseconds>(end - start).count()
    << " mcs" << endl;
    return 0;
}
