function generateSignature(name, title, company) {
  const rubric = (c) => {
    c = c.toLowerCase().charCodeAt()

    if(c >= "a".charCodeAt() && c <= "i".charCodeAt()) return ">>"
    if(c >= "j".charCodeAt() && c <= "r".charCodeAt()) return "--"
    if(c >= "s".charCodeAt() && c <= "z".charCodeAt()) return "::"

    return "lol"
  }

  return `${rubric(name[0])}${name}, ${title} at ${company}`;
}

console.log(generateSignature("Quinn Waverly", "Founder and CEO", "TechCo"))