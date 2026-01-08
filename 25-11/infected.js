function infected(days) {
  let infected = 1

  for(let d = 1; d <= days; d++) {
    infected *= 2
    if(d % 3 === 0) infected -= Math.ceil(infected * .2)
  }

  return infected;
}

console.log(infected(1))