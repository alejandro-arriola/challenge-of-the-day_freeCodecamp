function navigate(commands) {
  let route = [ 'Home' ]
  let pointer = 0

  for(const command of commands) {
    if(command.startsWith('V')) {
      while(route.length > pointer + 1) {
        route.pop()
      }

      route.push(command.slice("Visit ".length))
      pointer++
          console.log(route, pointer)
      continue
    }

    if(command === "Back") {
      if(pointer >= 1) pointer--
          console.log(route, pointer)
      continue
    }

    if(command === "Forward") {
      if(pointer + 1 < route.length) pointer++
      continue
    }
  }

  return route[pointer];
}

console.log(navigate(["Visit About Us", "Back", "Forward"]))