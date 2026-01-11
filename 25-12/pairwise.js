function pairwise(arr, target) {
  let sum = 0

  for(const [i, v] of arr.entries()) {
    const remain = target - v
    const iTarget = arr.indexOf(remain) 
    
    if(iTarget !== -1) {
      if(i !== iTarget) sum += i + iTarget
    }
  }

  return sum / 2
}

console.log(pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24))