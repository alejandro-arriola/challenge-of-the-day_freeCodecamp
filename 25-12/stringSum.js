function stringSum(str) {
  const numbers = str.match(/(\d+)/g)
  return numbers.reduce((acc, n) => acc + parseInt(n), 0);
}

console.log(stringSum("10cats5dogs2birds"))