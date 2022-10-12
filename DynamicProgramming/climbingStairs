/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    // if(n <= 1){
    //     return 1;
    // }else{
    //     return climbStairs(n -1) + climbStairs(n -2)
    // }
    let a = 1;
    let b = 0;
    let c = 0;
    for(let i = 0; i < n; i++){
     c = a;
     a += b;
     b = c;
    }
    return a;

};

//this problem is the fibonacci sequence
//lines 6-10 are a recursive solution it does not run as well as the other solution