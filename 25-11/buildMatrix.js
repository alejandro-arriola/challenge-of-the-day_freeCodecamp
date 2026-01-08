function buildMatrix(rows, cols) {
  return Array.from({length:rows}, v => Array.from({length:cols}, v => 0));
}

console.log(buildMatrix(2, 3))