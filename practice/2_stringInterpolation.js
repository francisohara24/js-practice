/**
 * @file   2_stringInterpolation.js
 * @brief  A program to demonstrate string interpolation syntax in JavaScript.
 * @author Francis O'Hara
 * @date   4/12/25
 */
let meaning_of_life = 42;
let string = `${meaning_of_life} is the meaning of Life, the Universe, and Everything.`;
console.log(string);

let animals = ["Birds", "Dogs", "Cats", "Lizards"]
console.log(`${animals} are examples of animals in the real world`);

/**
 * CONCLUSIONS
 *  1. String interpolation allows embedding anything that evaluates to a value's string representation into an existing string
 *     in a concise manner (i.e. cleaner alternative to string concatenation).
 *  2. The string must be enclosed in backticks ` instead of the usual quotes "" or ''.
 *  3. The value to be interpolated must be enclosed in curly brackets prepended with a dollar sign ${}.
 */