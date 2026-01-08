function getExtension(filename) {
  const fn = filename.split(".")
  const ext = fn.at(-1)

  if(fn.length === 1) return "none"
  if(ext === "") return "none"

  return ext
}

console.log(getExtension("README"))