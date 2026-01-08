function daysUntilWeekend(dateString) {
  const [y, m, d] = dateString.split("-")

  const date = new Date(y, m-1, d)
  const dotw = date.getDay()

  if(dotw === 0 || dotw === 6) return "It's the weekend!"

  return `${6-dotw} day${6-dotw === 1? "": "s"} until the weekend.`
}

console.log(daysUntilWeekend("2025-12-06"))