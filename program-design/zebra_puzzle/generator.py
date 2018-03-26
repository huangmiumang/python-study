def c(sequence):
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item

l = [1, 2, 3]
mygen = c(l)
print next(mygen)
