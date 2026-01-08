function compare(secret, guess) {
  const n = secret.length;
  const result = Array(n).fill("0");
  const freq = new Map();

  // Count frequency of each letter in secret
  for (const ch of secret) {
    freq.set(ch, (freq.get(ch) || 0) + 1);
  }

  // First pass: exact matches ("2")
  for (let i = 0; i < n; i++) {
    if (guess[i] === secret[i]) {
      result[i] = "2";
      freq.set(guess[i], freq.get(guess[i]) - 1);
    }
  }

  // Second pass: partial matches ("1")
  for (let i = 0; i < n; i++) {
    if (result[i] === "0") {
      const g = guess[i];
      if (freq.get(g) > 0) {
        result[i] = "1";
        freq.set(g, freq.get(g) - 1);
      }
    }
  }

  return result.join("");
}

console.log(compare("APPLE", "POPPA")); // "10201"
