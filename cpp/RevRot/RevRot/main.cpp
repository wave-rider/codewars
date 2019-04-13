//
//  main.cpp
//  RevRot
//
//  Created by wasabi on 9/04/19.
//  Copyright © 2019 wasabi. All rights reserved.
//

#include <iostream>
#include "RevRot.hpp"

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << RevRot::revRot("12345678", 6) << std::endl;
    std::cout << RevRot::revRot("123456987654", 6)<< std::endl; //--> "234561876549"
    std::cout << RevRot::revRot("123456987653", 6)<< std::endl; //--> "234561356789"
    std::cout << RevRot::revRot("66443875", 4)<< std::endl; //--> "44668753"
    std::cout << RevRot::revRot("66443875", 8)<< std::endl; //--> "64438756"
    std::cout << RevRot::revRot("664438769", 8)<< std::endl; //--> "67834466"
    std::cout << RevRot::revRot("123456779", 8)<< std::endl; //--> "23456771"
    std::cout << RevRot::revRot("", 8)<< std::endl; //--> ""
    std::cout << RevRot::revRot("123456779", 0)<< std::endl; //--> ""
    std::cout << RevRot::revRot("563000655734469485", 4)<< std::endl; // --> "0365065073456944"
    //330479108928157764
    std::cout << RevRot::revRot("733047910892815764", 15)<< std::endl;
    return 0;
}
