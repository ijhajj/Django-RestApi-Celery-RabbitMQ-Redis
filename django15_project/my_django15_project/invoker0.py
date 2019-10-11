from tasks import add

""" This is a producer that will cause the defined task to kick asynchronously """
add.delay(1, 3)
