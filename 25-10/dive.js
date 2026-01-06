function dive(map, coordinates) {
  const [ x, y ] = coordinates

  if(map[x][y] === '-') return "Empty"
  if(map[x][y] === 'X') return "Found"
  if(map[x][y] === 'O') {
    if(map.flat().filter(v => v === 'O').length > 1) return "Found"
  }
  
  return "Recovered"
}

console.log(dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]))