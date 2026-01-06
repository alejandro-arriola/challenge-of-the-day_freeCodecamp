function nthPrime(n) {
  function isPrime(num) {
    if (num < 2) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;

    const limit = Math.sqrt(num);

    for (let x = 3; x <= limit; x += 2) {
      if (num % x === 0) return false;
    }

    return true;
  }

  let count = 0;
  let candidate = 1;
  
  while (count < n) {
    candidate++;
    if (isPrime(candidate)) count++;
  }

  return candidate;
}

console.log(nthPrime(5));
