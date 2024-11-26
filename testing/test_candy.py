from dessert import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_Candy():
    item1 = Candy("Lollipop", 4.5, 2.00)
    item2 = Candy("Slurpables", 1.0, 2.0)
    item3 = Candy("Skittles", 2.4, 3.00)
    assert item1.name == "Lollipop"
    assert item2.candy_weight == 1.0
    assert item3.price_per_pound == 3.00