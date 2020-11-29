
import uuid

from log_orm import logger


class Review:
    def __init__(self, customer, item, rate):
        self.id = uuid.uuid4()
        self.customer = customer
        self.item = item
        self.rate = rate
        self.status = "Moderation"

    def validate_review(self):
        if str(self.rate).isdigit() and self.rate in range(1,6):
            logger.debug("Review is validated")
            return True
        return False

    def __str__(self):
        if not self.validate_review():
            logger.error(f"Error. Invalid rate '{self.rate}'. Should input from 1 to 5")
            exit()
        return f"Customer: {self.customer.first_name} rated {self.item.title} for {self.rate} points"

if __name__ == '__main__':
    from item import Item
    from customer import Customer

    c1 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                "guido@python.org", "09-09-1968")
    i1 = Item("Banana", "Better than ever you tried before", 809.90, ("Yellow", "Fish Yellow"))
    r1 = Review(c1, i1, 5)
    print(r1)