function complementaryDNA(strand) {
  return strand.split("").map(c => {
    switch(c) {
      case "A": return "T"
      case "T": return "A"
      case "C": return "G"
      default: return "C" //"G"
    }
  }).join("");
}

console.log(complementaryDNA("GGCTTACGATCGAAG"))