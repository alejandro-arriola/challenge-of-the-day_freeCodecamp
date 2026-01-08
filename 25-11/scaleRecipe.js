function scaleRecipe(ingredients, scale) {
  const pattern = /\d+(\.\d+)?/g

  return ingredients.map(i => i.replace(pattern, quantity => quantity * scale))
}

console.log(scaleRecipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5) )