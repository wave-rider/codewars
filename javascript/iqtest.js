 ///////////
  function iqTest(numbers){
    var array1 = numbers.split(" ")
    var length = array1.length
    var array=[]
    for(index=0; index<length; index++) 
    {
        array[index] = parseInt(array1[index])
    }
 
    found_index = 0
    
    var odd = 0
    var even = 0
    var all_odds = false
    for(index=0; index<length; index++) 
    {
         if (array[index]%2==0)
            even++
         else
            odd++;
        if (odd>1)
        {
            all_odds = true
            break;
        }
        if (even>1) 
        {
            break;
        }
    }
    for (index=0; index<length; index++)
    {
        elem = array[index]%2;
        if ((elem==0 && all_odds==true) || (elem!=0 && all_odds==false))
            return index + 1
    }
 
    return found_index;
   }
  console.log(iqTest("2 4 7 8 10")); //3
  console.log(iqTest("1 2 2")); //1
  console.log(iqTest("1 4 6 8 10 12")); //??
  console.log(iqTest("2 2 4"));//3
  console.log(iqTest("5 4 3 0")); // 4 
  console.log(iqTest("3 4 5 11")); // 4
  
  
  

//2  4  7  8  11
//  2  3  1  3