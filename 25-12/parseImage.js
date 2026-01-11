function parseImage(markdown) {
  const re = /!\[(.*)\]\((.*)\)/g;
  console.log(markdown.match(re))
  return markdown.replace(re, '<img src="$2" alt="$1">')
}

console.log(parseImage("![Cute cat](cat.png)"))