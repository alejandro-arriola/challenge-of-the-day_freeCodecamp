function fizzBuzz(n) {
  return Array.from( { length:n }, (_, i) => i + 1).map(v => v % 15 === 0 ? "FizzBuzz" : (v % 3 === 0 ? "Fizz" : (v % 5 === 0 ? "Buzz" : v)));
}