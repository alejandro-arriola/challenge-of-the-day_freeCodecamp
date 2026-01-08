function isValidMessage(message, validator) {
  message = message.toLowerCase().split(" ")
  validator = validator.toLowerCase().split("")

  if(message.length !== validator.length) return false

  for(const[i, m] of message.entries()) {
    if(!(m.startsWith(validator[i]))) return false
  }

  return true;
}

console.log(isValidMessage("hello world", "hw"))