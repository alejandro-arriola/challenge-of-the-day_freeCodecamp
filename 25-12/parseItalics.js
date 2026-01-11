function parseBold(markdown) {
  return markdown.replace(/\*\*(\S.*?\S)\*\*/g,"<b>$1</b>").replace(/__(\S.*?\S)__/g, "<b>$1</b>");
}

console.log(parseBold("The **quick** brown fox __jumps__ over the **lazy** dog."))