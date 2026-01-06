function sort(emails) {
  emails.sort((curr, next) => {
    let [ currName, currDomain ] = curr.split("@")
    let [ nextName, nextDomain ] = next.split("@")

    currName = currName.toLowerCase()
    currDomain = currDomain.toLowerCase()
    nextName = nextName.toLowerCase()
    nextDomain = nextDomain.toLowerCase()

    return currDomain.localeCompare(nextDomain) || currName.localeCompare(nextName) 
  });

  return emails
}

console.log(sort(["jill@mail.com", "john@example.com", "jane@example.com"]))