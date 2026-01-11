function difference(arr1, arr2) {
  let xArr1 = [...arr1]
  let xArr2 = [...arr2]

  for(const e of arr2) {
    if(xArr1.includes(e)) {
      xArr1 = xArr1.filter(v => v !== e)
      xArr2 = xArr2.filter(v => v !== e)
    }
  }

  return xArr1.concat(xArr2)
}

console.log(difference([1, 2, 3], [3, 4, 5]))