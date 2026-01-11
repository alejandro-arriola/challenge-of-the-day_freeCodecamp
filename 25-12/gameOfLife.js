function gameOfLife(grid) {
  const yLen = grid.length
  const xLen = grid[0].length

  const checkNs = (coords) => {
    let nOfNs = 0

    for(let j = -1; j <= 1; j++) {
      for(let i = -1; i <= 1; i++) {
        if(i === 0 && j === 0) continue
        let [ y, x ] = coords
        y += j
        x += i

        if(y === -1 || x === -1 || y === yLen || x === xLen) continue

        nOfNs += grid[y][x]
      }
    }

    return nOfNs
  }

  let result = grid.map(row => [...row])

  for(let y = 0; y < grid.length; y++) {
    for(let x = 0; x < grid[0].length; x++) {
      const score = checkNs([y, x])

      if(score < 2 || score > 3) result[y][x] = 0
      else if(score === 3) result[y][x] = 1 
    }
  }

  return result;
}

console.log(gameOfLife([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))