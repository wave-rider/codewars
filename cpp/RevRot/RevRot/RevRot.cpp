//
//  RevRot.cpp
//  RevRot
//
//  Created by wasabi on 9/04/19.
//  Copyright © 2019 wasabi. All rights reserved.
//

#include "RevRot.hpp"
#include <sstream>
#include <cmath>

std::string RevRot::revRot(const std::string &strng, unsigned int sz)
{
    if (sz<=0)
        return "";
    long number;
    auto string_length = strng.size();
    
    if (strng.size() < sz)
    {
        return "";
    }
    unsigned int index = 0;
    std::string result = "";
    std::string chunk = strng.substr(index, sz);
    do
    {
        std::istringstream stream (chunk);
        stream >> number;
        bool rotate_string = true;
        if (stream.fail() == false) {
            long sum=0;
            for (int i=0; i<sz; i++){
                int number_to_add = chunk[i] - 48;
                sum = sum + pow(number_to_add, 3);
            }
            if (sum % 2 ==0)
            {
                rotate_string = false;
            }
        }
        
        if (rotate_string==true)
        {
            // rotate string
            std::string part1 = chunk.substr(0, 1);
            std::string part2 = chunk.substr(1, sz - 1);
            std::string rotated = part2 + part1;
            result += rotated;
        }
        else
        {
            std::reverse(chunk.begin(),chunk.end());
            result += chunk;
        }
        index += sz;
        chunk = strng.substr(index, sz);
        if (chunk.size() < sz)
        {
            break;
        }
        
    }while (index < string_length);
 
    return result;
}






