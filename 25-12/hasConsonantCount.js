function hasConsonantCount(text, target) {
  return text.replace(/[^bcdfghjklmnpqrstvwxyz]/gi, "").length === target
}

console.log(hasConsonantCount("helloworld", 7))