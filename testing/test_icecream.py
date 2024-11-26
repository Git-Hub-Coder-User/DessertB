from dessert import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_IceCream():
    item1 = IceCream("Vanilla", 4, 2.00)
    item2 = IceCream("Chocolate", 2, 1.00)
    item3 = IceCream("Mint", 5, 2.49)
    assert item1.name == "Vanilla"
    assert item2.scoop_count == 2
    assert item3.price_per_scoop == 2.49
    assert item1.packaging == "Bowl"