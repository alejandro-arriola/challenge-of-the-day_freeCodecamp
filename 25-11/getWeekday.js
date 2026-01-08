function getWeekday(dateString) {
  const [ y, m, d] = dateString.split("-")
  const date = new Date(y, m - 1, d)
  const days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ]
  
  return days[date.getDay()];
}

console.log(getWeekday("2025-11-06"))