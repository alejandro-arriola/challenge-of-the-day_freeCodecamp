function count(str) {
  str = str.toLowerCase().split("")

  const vowels = str.filter(c => /[aeiou]/.test(c)).length
  const conso = str.filter(c => /[bcdfghjklmnpqrstvwxyz]/.test(c)).length

  return [ vowels, conso ];
}

console.log(count("Hello World"))