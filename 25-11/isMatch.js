function isMatch(fingerprintA, fingerprintB) {
  const lenA = fingerprintA.length
  const lenB = fingerprintB.length

  if (lenA !== lenB) return false;

  let differences = 0;

  for (let i = 0; i < lenA; i++) {
    if (fingerprintA[i] !== fingerprintB[i]) {
      differences++;
    }
  }

  return differences <= lenA * 0.1;
}

console.log(
  isMatch("theslickbrownfoxjumpsoverthelazydog", 
          "thequickbrownfoxjumpsoverthehazydog")
);
