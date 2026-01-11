function formatDate(dateString) {
  const [ m, d, y ] = dateString.split(" ")

  const meses = new Map([
    ["December", 12],
    ["November", 11],
    ["October", 10],
    ["September", "09"],
    ["August", "08"],
    ["July", "07"],
    ["June", "06"],
    ["May", "05"],
    ["April", "04"],
    ["March", "03"],
    ["February", "02"],
    ["January", "01"],
  ])

  return `${y}-${meses.get(m)}-${d.match(/\d+/)[0].padStart(2, "0")}`;
}

console.log(formatDate("December 6, 2025"))