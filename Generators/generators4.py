def generator_function():
    print('before yield')
    yield 10                            # yield makes it a generator
    print('before second yield')
    yield 20                            # second yield 


for value in generator_function():      # use generator in for loop
    print(value)