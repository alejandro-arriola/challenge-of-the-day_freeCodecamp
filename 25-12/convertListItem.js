function convertListItem(markdown) {
  const re = /\s*\d+.\s+(.*)/g

  if(!re.test(markdown)) return "Invalid format"

  return markdown.replace(re, "<li>$1</li>");
}

console.log(convertListItem("1. My item"))