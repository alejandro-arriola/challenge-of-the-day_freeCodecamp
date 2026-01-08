function imageSearch(images, term) {
  return images.filter(img => img.toLowerCase().includes(term.toLowerCase()));
}

console.log(imageSearch(["dog.png", "cat.jpg", "parrot.jpeg"], "dog"))