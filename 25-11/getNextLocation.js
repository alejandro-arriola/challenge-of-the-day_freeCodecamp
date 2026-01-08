function getNextLocation(matrix) {
  function pos(matrix, valueToSearch) {
    let [ y, x ] = [ 0, 0 ]
    for(const row of matrix) {
      for(const value of row) {
        if(value === valueToSearch) return [ y, x ]
        x++
      }
      y++
      x = 0
    }

    return null
  }

  const posOf2 = pos(matrix, 2)
  const posOf1 = pos(matrix, 1)

  if(!posOf1 || !posOf2) return []

  let newPos = [ posOf2[0], posOf2[1] ]

  newPos[0] += posOf2[0] < posOf1[0] ? -1 : posOf2[0] > posOf1[0] ? 1 : 0
  newPos[1] += posOf2[1] < posOf1[1] ? -1 : posOf2[1] > posOf1[1] ? 1 : 0

  //check borders
  if(newPos[0] === -1) newPos[0] = 1
  else if(newPos[0] === 4) newPos[0] = 2
  if(newPos[1] === -1) newPos[1] = 1
  else if(newPos[1] === 4) newPos[1] = 2

  return newPos;
}

console.log(getNextLocation([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]))