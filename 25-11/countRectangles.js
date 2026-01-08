function countRectangles(width, height) {
  return (width * (width + 1) / 2) * (height * (height + 1) / 2);
}

console.log(countRectangles(1, 2))