function convertToKgs(lbs) {
  const kilo = lbs * 0.453592
  return `${lbs} pound${lbs === 1 ? "" : "s"} equals ${kilo.toFixed(2)} kilogram${kilo >= 0.99 && kilo <= 1 ? "" : "s"}.` //have to condition by range due to floating precision
}

console.log(convertToKgs(2.20462))