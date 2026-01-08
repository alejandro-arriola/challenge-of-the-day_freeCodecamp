function calculateAge(birthday) {
  const [y, m, d] = birthday.split("-")
  let age = 2025 - y
  
  if(m > 11) age--
  if(m === 11 && d >= 27) age--

  return age;
}

console.log(calculateAge("2000-11-20"))