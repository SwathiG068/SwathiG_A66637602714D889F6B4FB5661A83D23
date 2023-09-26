def linear_search_product(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["books", "pens", "paper", "books", "pencil", "books"]
target = "books"
target2 = "Apple"
result = linear_search_product(products, target)
print(result)
#if the target value is not found
result2 = linear_search_product(products, target2)
print(result2)
