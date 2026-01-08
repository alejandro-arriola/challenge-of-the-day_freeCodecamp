function oneHundred(chars) {
  let result = chars

  while(result.length < 100) {
    result += chars
  }

  return result.slice(0, 100);
}

console.log(oneHundred("One hundred "))