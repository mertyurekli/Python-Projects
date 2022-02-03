edge1 = float(input("First edge: "))
edge2 = float(input("Second edge: "))

def pisagor(edge1, edge2):
    pisagor = (edge1**2 + edge2**2) ** 0.5

    return pisagor

print(pisagor(edge1, edge2))