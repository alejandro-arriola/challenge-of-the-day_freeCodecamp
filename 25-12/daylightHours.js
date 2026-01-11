function daylightHours(latitude) {
  const l = latitude
  const half = 7.5

  if(l < -90 + half) return 24
  if(l < -75 + half) return 23
  if(l < -60 + half) return 21
  if(l < -45 + half) return 15
  if(l < -30 + half) return 13
  if(l < -15 + half) return 12
  if(l < 0 + half) return 12
  if(l < 15 + half) return 11
  if(l < 30 + half) return 10
  if(l < 45 + half) return 9
  if(l < 60 + half) return 6
  if(l < 75 + half) return 2

  return 0;
}

console.log(daylightHours(-33))