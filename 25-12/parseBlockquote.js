function parseBlockquote(markdown) {
  return `<blockquote>${markdown.replace(/\s*>\s*/, "")}</blockquote>`;
}

console.log(parseBlockquote("  >    So  Is  This"))