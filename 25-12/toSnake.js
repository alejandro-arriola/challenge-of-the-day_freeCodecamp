function toSnake(camel) {
  return camel.replace(/([A-Z])/g, (match) => "_" + match.toLowerCase());
}

console.log(toSnake("myVariableName"))