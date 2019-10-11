from tasks import add

""" This is a producer that will cause the defined task to kick asynchronously """
""" This version is returning the result in a variable and using the get function to display the total """
result = add.delay(1, 3)
print(result.get())
