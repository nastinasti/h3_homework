from user import User
from customer import Customer
from admin import Administrator
from supplier import Supplier
from log_orm import logger
from item import Item
from supply import Supply
from order import Order

supply = list()
orders = list()
item = list()

admin1 = Administrator("iamgod", "iamthelaw", "memyself@heavens.com")
supplier1 = Supplier("isupply", "4real", "Crab Shack Company", "Van Crabs",
                    "000-112-35-8", "crab@shack.biz")
supplier2 = Supplier("isupplytoo", "4real", "Reliable Company", "Van Reliable",
                    "011-112-35-8", "no-reply@reliable.biz")
customer1 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                    "guido@python.org", "09-09-1968")
customer2 = Customer("_iamguido", "_4sure", "_Guido", "_Van Rossum", "000-112-35-8",
                    "_guido@python.org", "09-09-1968")
item1 = Item("Banana", "Better than ever before", 799.0,
            ("Golden", "Fresh Green"))
item2 = Item("Best Banana", "Better than others", 899.0,
            ("Truly Golden", "Fresher Green"))

supply.append(supplier1.add_supply(item1, 10))
supply.append(supplier2.add_supply(item2, 5))

customer1.create_order(item2, 5)
logger.info(customer1.orders[0].status)
customer1.create_review(item1, 10)
logger.info(customer1.reviews[0].status)

customer2.create_order(item1, 4)
logger.info(customer2.orders[0].status)
customer2.create_review(item1, 4)
logger.info(customer2.reviews[0].status)

admin1.update_supply([supplier1, supplier2])
admin1.update_orders([customer1, customer2])
admin1.update_reviews([customer1, customer2])

admin1.check_order(customer1.orders[0])
admin1.check_review(customer1.reviews[0])
logger.info(customer1.orders[0].status)
logger.info(customer1.reviews[0].status)

admin1.check_order(customer2.orders[0])
admin1.check_review(customer2.reviews[0])
logger.info(customer2.orders[0].status)
logger.info(customer2.reviews[0].status)