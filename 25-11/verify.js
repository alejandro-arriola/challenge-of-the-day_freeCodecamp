function verify(message, key, signature) {
  function letterToNumber(letter) { 
    const code = letter.charCodeAt(0)
    
    if (code >= 97 && code <= 122) return code - 96  
    if (code >= 65 && code <= 90) return code - 65 + 27
  }
  
  const m = message.replace(/[^a-z]/gi, "").split("").map(c => letterToNumber(c)).reduce((curr, next) => curr + next, 0)
  const k = key.replace(/[^a-z]/gi, "").split("").map(c => letterToNumber(c)).reduce((curr, next) => curr + next, 0)

  return m + k === signature;
}

console.log(verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514)) //should return true