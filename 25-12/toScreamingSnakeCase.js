function toScreamingSnakeCase(variableName) {
  return variableName.replace(/(?<=.)([A-Z])/g, (match) => "_" + match).replace(/(-)/, "_").toUpperCase()
}

console.log(toScreamingSnakeCase("user-address"))