 // TODO: return a function that loops through 'str' on successive invocations
function makeLooper(str) {
    var a = 0;
    var counter = str.length;
    var str = str;
    return function()
    {
        if (a==str.length)a=0;
        a++;
        return str[a-1]
    }
}

var abc = makeLooper('Hello');
console.log(abc());
console.log(abc());
console.log(abc());
console.log(abc());