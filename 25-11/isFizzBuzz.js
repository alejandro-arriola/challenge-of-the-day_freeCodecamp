function isFizzBuzz(sequence) {
  for(const [i, n] of sequence.entries()) {
    const ind = i + 1
    
    if(Number.isInteger(n)) {
      if(n !== ind) return false
      if(n % 3 === 0 || n % 5 === 0) return false

      continue
    }
    
    if(ind % 15 === 0) {
      if(n !== "FizzBuzz") return false
      else continue
    }

    if(ind % 3 === 0) {
      if(n !== "Fizz") return false 
      else continue
    }

    if(ind % 5 === 0) {
      if(n !== "Buzz") return false
      else continue
    }

    //else
    return false
  }

  return true;
}

console.log(isFizzBuzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]))