//wololooo!
function convert(heading) {
  const pattern = /^\s*(#{1,6})\s+(.*)$/

  if(!pattern.test(heading)) return "Invalid format"
  
  const data = heading.match(pattern)
  const hLength = data[1].length

  return `<h${hLength}>${data[2]}</h${hLength}>`
}

console.log(convert("# My level 1 heading"))