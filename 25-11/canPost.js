function canPost(message) {
  const len = message.length
  
  if(len <= 40) return "short post"
  if(len <= 80) return "long post"
  return "invalid post";
}

console.log(canPost("Hello world"))