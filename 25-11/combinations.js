//this is a math problem, not a programming one
function combinations(cards) {
  const factorial = (n) => n === 0 ? 1 : n * factorial(n - 1)
  const combinations = (n, k) => factorial(n) / (factorial(k) * factorial(n - k))

  return combinations(52, cards);
}