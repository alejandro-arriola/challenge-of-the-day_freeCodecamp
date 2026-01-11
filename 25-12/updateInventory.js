function updateInventory(inventory, shipment) {
  inventory.forEach(row => row.reverse())
  inventory = new Map(inventory)

  for(const item of shipment) {  
    inventory.set(item[1], (inventory.get(item[1]) || 0) + item[0] )
  }
  
  inventory = [...inventory]
  inventory.forEach(row => row.reverse())

  return inventory
}

console.log(updateInventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]))