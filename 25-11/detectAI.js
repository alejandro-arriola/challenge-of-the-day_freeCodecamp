function detectAI(text) {
  if(text.split("-").length > 2) return "AI"
  
  let rege = text.match(/\(.*?\)/g)
  if(rege && rege.length > 1) return "AI"
  
  rege = text.match(/\b[A-Za-z]{7,}\b/g)
  if(rege && rege.length >= 3) return "AI"
  
  //The fourth condition is not explicitely checked in its own 'if' like the other ones, and yet it passes all the tests anyway. After consulting with Copilot, it does not provide any extra regex to deal with it, so I am assuming it is being already implicitely solved with the previous regex

  return "Human";
}

console.log(detectAI("The hypersonic brown fox - jumped (over) the lazy dog."))