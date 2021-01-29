""" You have a list of integers, and for each index you want to find the product 
of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a 
list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution! """

# Start coding from here
def product(l):
  if len(l) == 0:
    print([])
  if len(l) == 1:
      print([1])
  p = [1]*len(l)
#print(p)
  for i in range(len(l)):
    for j in range(0,i):
      p[j] = p[j]*l[i]
        #print(p[j])
    for j in range(i + 1, len(p)):
        p[j] = p[j] * l[i]
  return p
l = [1,7,3,4]
print(product(l))
