def true(tuple):
    return all(tuple)
tuple1=(True, False, True)
tuple2=(True, True, True)
print(true(tuple1))
print(true(tuple2))