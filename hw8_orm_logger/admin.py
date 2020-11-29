import uuid
from user import User
from log_orm import logger

class Administrator(User):
    def __init__(self, username, userpass, email):
        super().__init__(username, userpass, email)
        self.supply = list()
        self.orders = list()
        self.reviews = list()

    def update_supply(self, suppliers_list):
        self.supply.clear()
        for supplier in suppliers_list:
            logger.info(f"Supply {supplier} is updated by administrator")
            self.supply.extend(supplier.supply)

    def update_orders(self, customers_list):
        self.orders.clear()
        for customer in customers_list:
            self.orders.extend(customer.orders)

    def check_order(self, order):
        logger.debug(f"Checking orders {order.id}")
        if not order.status == 'New':
            return order
        for supply in self.supply:
            if supply.item == order.item and supply.amount >= order.amount:
                order.status = 'Confirmed'
                logger.info(f"New order: {order}, is confirmed")
                return order
        order.status = 'On Hold'
        return order

    def check_review(self, review):
        logger.debug(f"Checking reviews {review.id}")
        if not review.validate_review():
            logger.error(f"Error. Invalid rate '{review.rate}'. Should input rate from 1 to 5")
            exit()
        if not review.status == 'Moderation':
            return review
        for rate in self.reviews:
            if rate.item == review.item:
                review.status = 'Published'
                logger.info(f"New review by {review}, is published")
                return review
        review.status = 'Not confirmed'
        return review

    def update_reviews(self, reviews):
        self.reviews.clear()
        for customer in reviews:
            logger.debug("Review is updated")
            self.reviews.extend(customer.reviews)
