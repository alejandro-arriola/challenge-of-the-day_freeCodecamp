function shiftArray(arr, n) {
  while(n > 0) {
    const v = arr.shift()
    arr.push(v)
    n--
  }

  while(n < 0) {
    const v = arr.pop()
    arr.unshift(v)
    n++
  }

  return arr;
}

console.log(shiftArray([1, 2, 3], 1))