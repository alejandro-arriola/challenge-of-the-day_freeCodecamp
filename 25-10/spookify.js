function spookify(boo) {
  function isAlphabetic(char) {
    return /^[A-Za-z]$/.test(char)
  }

  let flag = true
  let result = ""

  boo = boo.split("")

  for(const c of boo) {
    if(isAlphabetic(c)) {
      result += flag ? c.toUpperCase() : c.toLowerCase()
      flag = !flag
    } else {
      result += "~"
    }
  }

  return result;
}

console.log(spookify("hello_world"))