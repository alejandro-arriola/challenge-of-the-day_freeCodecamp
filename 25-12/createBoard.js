function createBoard(dimensions) {
  const sY = dimensions[0]
  const sX = dimensions[1]
  let board = Array.from({length:sY}, v => Array.from({length:sX}, v => "-"))

  for(let y = 0; y < sY; y++) {
    let isX = y % 2 === 0

    for(let x = 0; x < sX; x++) {
      board[y][x] = isX ? "X" : "O"
      isX = !isX
    }
  }

  return board;
}

console.log(createBoard([2, 10]))