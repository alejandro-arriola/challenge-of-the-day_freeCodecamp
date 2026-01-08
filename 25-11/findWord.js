function findWord(matrix, word) {
  const buscador = (matr, target, tegrat) => {
    for(const [ i, w ] of matr.entries()) {
        if(w.includes(target)) {
          return [[ i, w.indexOf(target[0]) ], [ i, w.indexOf(target.at(-1)) ]]
        } else if(w.includes(tegrat)) {
          return [[ i, w.indexOf(tegrat.at(-1)) ], [ i, w.indexOf(tegrat[0]) ]]
        }
    }
  }

  //left-to-right and right-to-left
  const reversedWord = word.split("").reverse().join("")
  let mat = matrix.map(row => row.join(""))

  let coords = buscador(mat, word, reversedWord)
  if(coords) return coords

  //up-to-down and down-to-up
  //transpose matrix
  mat = matrix[0].map((_, colIndex) => matrix.map(row => row[colIndex])).map(row => row.join("")) 
  coords = buscador(mat, word, reversedWord)
  if(coords) return coords.map(row => [ row[1], row[0] ])
}

console.log(findWord([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat"))//should return [[0, 1], [2, 1]]
console.log(findWord([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog")) //should return [[0, 0], [0, 2]]
console.log(findWord([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish")) //should return [[3, 3], [0, 3]]
console.log(findWord([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox")) //should return [[1, 3], [1, 1]]