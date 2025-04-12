/**
 * @file   1_javascriptArrays.js
 * @brief  A program to demonstrate syntax for creating and using arrays in JavaScript.
 * @author Francis O'Hara
 * @date   4/12/25
 */

/** declaring arrays */
let arr = [1, 2.0, "three", true, null];
let arr2 = new Array(1, 2.0, "three", true, null);
console.log("arr: " + arr);
console.log("arr2: " + arr2 + "\n");

/** getting length of arrays */
console.log("arr length: " + arr.length + "\n");

/** indexing arrays */
console.log(arr[2])     // Output: "three"
console.log(arr[4] + "\n")     // Output: null

/** slicing arrays */
console.log("slice from 1 to 3: " + arr.slice(1, 3) + "\n")    // Output: [2, "three"]

/** push item to end of array */
console.log("Before Push: " + arr);
arr.push(42);
console.log("After Push: " + arr + "\n");

/** remove item from end of array (pop) */
console.log("Before Pop: " + arr);
arr.pop();
console.log("After Pop: " + arr + "\n");

/** add item to beginning of array */
console.log("Before Unshift: " + arr);
arr.unshift(0);
console.log("After Unshift: " + arr + "\n");

/** remove item from beginning of array */
console.log("Before Shift: " + arr);
arr.shift();
console.log("After Shift: " + arr + "\n");

/** check if array contains item */
console.log("Is \"three\" in array? " + arr.includes("three"));

/** get index of item in array */
console.log("The index of `true` in arr is: " + arr.indexOf(true));

/** Iterate over array elements with value-based for loop */
for(let item of arr){
    console.log(`${arr.indexOf(item)}: ${item}`);
}