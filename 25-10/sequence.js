function sequence(n) {
  return Array.from({ length:n }, (curr, index) => index + 1).join("");
}

console.log(sequence(10))