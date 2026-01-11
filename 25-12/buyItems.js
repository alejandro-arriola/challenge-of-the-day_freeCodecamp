function buyItems(funds, items) {
  const conv_table = new Map([["USD", 1], ["EUR", 1.1], ["GBP", 1.25], ["JPY", 0.007], ["CAD", 0.75]])

  let count = 0

  let f = funds[0] * conv_table.get(funds[1])

  for(const item of items) {
    const i = item[0] * conv_table.get(item[1])

    if(i <= f) {
      f -= i
      count++
    } else {
      break
    }
  }

  return count === items.length ? "Buy them all!" : `Buy the first ${count} item${count === 1 ? "" : "s"}.`;
}

console.log(buyItems(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]))