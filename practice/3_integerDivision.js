/**
 * @file   3_integerDivision.js
 * @brief  Program to demonstrate integer division in JavaScript.
 * @author Francis O'Hara
 * @date   4/12/25
 */
let dividend = 3;
let divisor = 2;

/** Regular division in JavaScript (float division) */
console.log("regular division: " + dividend/divisor);

/** integer division with Math.trunc() */
console.log("Math.trunc() division: " + Math.trunc(dividend/divisor));

/** integer division with Math.floor() */
console.log("Math.floor() division: " + Math.floor(dividend/divisor));

/** Math.floor() with negative float argument */
console.log("Math.floor(-1.9): " + Math.floor(-1.9));

/** Math.trunc() with negative float argument */
console.log("Math.trunc(-1.9): " + Math.trunc(-1.9));

/**
 * CONCLUSIONS
 *      1. Since JavaScript has no built-in integer division operator or integer datatypes, the Math.trun() and Math.floor()
 *         methods must be used to achieve integer division.
 *      2. Math.trunc() truncates or cuts off the fractional part of the input Number.
 *      3. Math.floor() rounds down the given input number to the closest integer less than the input number.
 *      4. For non-negative numbers, Math.trunc() and Math.floor() yield the same result, but for negative numbers, Math.floor()
 *         yields a different result from Math.trunc() as simply getting rid of the fractional part of a given negative number
 *         will not result in the closest integer less than the given negative number.
 *
 *
 */