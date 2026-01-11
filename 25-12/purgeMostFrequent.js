function purgeMostFrequent(arr) {    
  let freq = {}
  arr.forEach(v => freq[v] = (freq[v] || 0) + 1)
  freq = Object.entries(freq).sort((a, b) => b[1] - a[1])
  const mostFreq = freq[0][1]
  let submostFreq = 0

  do {
    arr = arr.filter(v => v != freq[0][0])
    if(arr) break //the condition was meant to be 'arr === []', but it threw an error. However, it works with just 'arr' for some reason
    freq.shift()
    submostFreq = freq[0][1]
  } while(submostFreq === mostFreq)

  return arr
}

console.log(purgeMostFrequent([1, 2, 2, 3]))