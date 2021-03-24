def squares(*args):
    import statistics
    if len(args) == 1:
        return print("Σφάλμα: Δώστε πάνω από έναν αριθμούς")
    else:
        for i in args:
            yield (i-statistics.mean(args))**2

for k in squares(3,4,5):
    print(k)
