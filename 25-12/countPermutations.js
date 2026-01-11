//another math problem, solved by applying the formula of permutations for duplicatesinto code
function countPermutations(str) {
  const factorial = (num) => {
    let fact = 1;
    for (let i = 2; i <= num; i++) fact *= i;
    return fact;
  };

  const n = str.length;
  const counts = {};

  for (let char of str) {
    counts[char] = (counts[char] || 0) + 1;
  }

  let denominator = 1;

  for (let char in counts) {
    denominator *= factorial(counts[char]);
  }

  return factorial(n) / denominator;
}
