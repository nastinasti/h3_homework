'''
-----Customer Class. Has access only to customer issues
'''

import uuid

from user import User
from order import  Order
from review import Review
from log_orm import logger

class Customer(User):
    def __init__(self, username, userpass, first_name, last_name,
                 email, phone, date_of_birth):
        super().__init__(username, userpass, email)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.bonus_amount = 0
        self.orders = list()
        self.reviews = list()

    def __str__(self):
        return f"Customer {self.id}: {self.username} ({self.first_name}\"" \
               f"{self.last_name} {self.phone})"

    def create_order(self, item, amount):
        new_order = Order(self, item, amount)
        self.orders.append(new_order)
        logger.info(f"New order, {new_order} is created by the customer: {self.id}")
        return new_order

    def create_review(self, item, rate):
        new_review = Review(self, item, rate)
        self.reviews.append(new_review)
        logger.info(f"New review by {new_review}, is created by the customer: {self.id}")
        return new_review


if __name__ == '__main__':
    from item import Item

    c1 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                "guido@python.org", "09-09-1968")
    i1 = Item("Banana", "Better than ever before", 799.0,
                ("Golden", "Fresh Green"))
    c1.create_order(i1, 3)
    print(c1)
    print(c1.orders)

