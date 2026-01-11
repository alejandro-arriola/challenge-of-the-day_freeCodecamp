function titleCase(title) {
  return title.toLowerCase().split(" ").map(w => w[0].toUpperCase() + w.slice(1)).join(" ")
}

console.log(titleCase("AvOcAdO tOAst fOr brEAkfAst"))