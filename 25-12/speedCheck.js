function speedCheck(speedMph, speedLimitKph) {
  const speedLimitMph = speedLimitKph / 1.60934
  const warningLimit = 5 / 1.60934

  if(speedMph <= speedLimitMph) return "Not Speeding"
  if(speedMph <= speedLimitMph + warningLimit) return "Warning"

  return "Ticket";
}

console.log(speedCheck(40, 60))