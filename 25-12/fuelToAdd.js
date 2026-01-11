function fuelToAdd(currentGallons, requiredLiters) {
  const wololo = (liters) => liters / 3.78541
  const requiredGallons = wololo(requiredLiters)

  if(currentGallons >= requiredGallons) return 0

  return Math.ceil(requiredGallons - currentGallons)
}

console.log(fuelToAdd(5, 40))