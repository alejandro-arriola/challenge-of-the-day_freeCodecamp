function countCharacters(sentence) {
  const pattern = /[^a-z]/ig

  sentence = sentence.replaceAll(pattern, "").toLowerCase()
  let result = new Map([...new Set(sentence)].sort().map(k => [k, 0]))

  for(const s of sentence) {
    result.set(s, result.get(s) + 1)
  }

  return [...result].map(pair => `${pair[0]} ${pair[1]}`);
}

console.log(countCharacters("I love coding challenges!"))