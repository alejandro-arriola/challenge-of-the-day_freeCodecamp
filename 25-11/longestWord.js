function longestWord(sentence) {
  const pattern = /\w+/g
  return sentence.replaceAll("'","").match(pattern).sort((a, b) => b.length - a.length)[0];
}

console.log(longestWord("The quick red fox"))