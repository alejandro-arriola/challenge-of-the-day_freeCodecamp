function sumDivisors(n) {
  return Array.from({ length:n }, (_, i) => i + 1).reduce((acc, next) => n % next === 0 ? acc + next : acc, 0)
}

console.log(sumDivisors(6))