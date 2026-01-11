function rockPaperScissors(player1, player2) {
  const rpsTable = {
    "Paper" : "Scissors",
    "Rock" : "Paper",
    "Scissors" : "Rock",
  }

  if(player1 === rpsTable[player2]) return "Player 1 wins"
  if(player2 === rpsTable[player1]) return "Player 2 wins"

  return "Tie";
}

console.log(rockPaperScissors("Rock", "Paper"))