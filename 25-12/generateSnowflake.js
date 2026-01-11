function generateSnowflake(crystals) {
  return crystals.split("\n").reduce((acc, v) => acc += v + v.split("").reverse().join("") + "\n" , "").replace(/\n$/, "");
}

console.log(generateSnowflake(" X  \n  v \nX--=\n  ^ \n X  "))