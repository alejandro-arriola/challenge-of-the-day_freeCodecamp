function format(seconds) {
  let hours = 0

  if(seconds >= 3600) {
    hours += Math.floor(seconds / 3600)
    seconds -= (hours * 3600)
  }

  let minutes = 0

  if(seconds >= 60) {
    minutes += Math.floor(seconds / 60)
    seconds -= minutes * 60
  }  

  if(hours > 0) {
    return `${hours}:${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
  }

  if(minutes > 0) {
    return `${minutes}:${String(seconds).padStart(2, "0")}`
  }

  //only has seconds
  return `0:${String(seconds).padStart(2, "0")}`
}

console.log(format(500))