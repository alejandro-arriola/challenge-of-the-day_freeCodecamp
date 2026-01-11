function compressString(sentence) {
  let wordsFreq = new Map()

  sentence.split(" ").forEach(w => {
    wordsFreq.set(w, (wordsFreq.get(w) || 0) + 1)
  })
  
  return [...wordsFreq].map(w => w[1] !== 1 ?`${w[0]}(${w[1]})`: w[0]).join(" ")
}

console.log(compressString("yes yes yes please")) //🗿