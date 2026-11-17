def parametry(*args):
    for parametr in args:
        print(parametr)

parametry(1, 2, 3, 4, 5)
parametry("Python", "Java", "C++")

def maksimum(*args):
    if len(args) == 0:
        return None
    return max(args)

print(f"Największa wartość wynosi: {maksimum(5, 10, 3, 8)}")