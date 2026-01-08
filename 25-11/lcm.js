function lcm(a, b) {
  let aa = a < b ? a : b
  let bb = [ a > b ? a : b ]

  const xa = aa
  const xb = bb[0]

  while(aa <= bb[bb.length - 1]) {
    if(bb.includes(aa)) return aa

    aa += xa
    bb.push(bb[bb.length - 1] + xb)
  }
  
  return a * b;
}

console.log(lcm(9, 6))