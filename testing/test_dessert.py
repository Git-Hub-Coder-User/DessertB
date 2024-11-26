from dessert import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_DessertItem():
    item1 = Candy("Pie")
    item2 = Candy("Cake")
    item3 = Candy("Cakepop")
    assert item1.name == "Pie"
    assert item2.name == "Cake"
    assert item3.name == "Cakepop"