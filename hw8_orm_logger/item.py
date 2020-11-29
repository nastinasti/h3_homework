import uuid


class Item:
    def __init__(self, title, description, price, colours=("Black",)):
        self.id = uuid.uuid4()
        self.title = title
        self.description = description
        self.price = price
        self.colours = colours

    def __str__(self):
        return f"Item: {self.id} {self.title} ${self.price}"

    def __repr__(self):
        return f"Item {self.id}: {self.title}"

if __name__ == '__main__':
    i1 = Item("Banana", "Better than ever you tried before", 809.90, ("Yellow", "Fish Yellow"))
    print(i1)