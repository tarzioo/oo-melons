from random import randint
import datetime

"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """The basic structure of the melon order."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.order_time = datetime.datetime.now()

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):
        """Use random module for splurge pricing"""

        splurge_price = randint(4, 9)

        is_weekday = self.order_time.weekday() in range(5)
        is_rushhour = self.order_time.hour in range(8,11)

        if is_weekday and is_rushhour: 
            splurge_price += 4


        return splurge_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Adding fee for international orders with small quantities."""

        total = super(InternationalMelonOrder, self).get_total()
        if (self.order_type == "international") and (self.qty < 10):
            total += 3

        return total
            


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0.0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Return the inspection status"""

        self.passed_inspection = passed

        return self.passed_inspection