//had to use the JSON because otherwise test 3 (with values true and false) would fail despite the output and the expected output to be the same
function mostFrequent(arr) {
  arr = arr.reduce((acc, v) => {
    const key = JSON.stringify(v)
    acc[key] = (acc[key] || 0 ) + 1
    return acc
  }, {})

  const [key] = Object.entries(arr).sort((a, b) => b[1] - a[1])[0]

  return JSON.parse(key)
}

console.log(mostFrequent([true, false, "false", "true", false]))