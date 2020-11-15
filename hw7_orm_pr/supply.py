import uuid


class Supply:
    def __init__(self, item, supplier, amount):
        self.id = uuid.uuid4()
        self.item = item
        self.supplier = supplier
        self.amount = amount

    def __str__(self):
        return f"{self.id}: {self.item} by {self.supplier}"

    def __repr__(self):
        return f"{self.id}: {self.amount} {self.item.title} by {self.supplier.company_name}"

if __name__ == '__main__':
    from item import Item
    from supplier import Supplier

    i1 = Item("Banana", "Better than ever you tried before", 809.90, ("Yellow", "Fish Yellow"))
    s1 = Supplier("isupply", "4real", "Crab Shack Company", "Van Crabs",
                  "000-112-35-8", "crab@shack.biz")
    sup1 = Supply(i1, s1, 3)
    print(sup1)