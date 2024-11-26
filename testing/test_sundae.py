from dessert import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_Sundae():
    item1 = Sundae("Vanilla", 3, 2.00, "Sprinkles", 1.00)
    item2 = Sundae("Chocolate", 4, 1.00, "Chocolate chips", 0.45)
    item3 = Sundae("Mint", 1, 2.49, "Cherry", 3.00)
    assert item1.name == "Vanilla"
    assert item2.scoop_count == 4
    assert item2.price_per_scoop == 1.00
    assert item3.topping_name == "Cherry"
    assert item3.topping_price == 3.00