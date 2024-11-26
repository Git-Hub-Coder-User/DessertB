from dessert import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_Cookie():
    item1 = Cookie("Chocolate chip cookies", 4, 2.45)
    item2 = Cookie("Blondie bites", 10, 2.01)
    item3 = Cookie("Lemon cookies", 7, 3.00)
    assert item1.name == "Chocolate chip cookies"
    assert item2.quantity == 10
    assert item3.price_per_dozen == 3.00
    assert item1.packaging == "Box"