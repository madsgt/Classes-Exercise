"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """A parent class to model domestic and international classes"""

    def __init__(self,species,qty,tax,order_type,flat_fee=0):
        self.species = species
        self.qty = qty
        self.shipped = False 
        self.tax = tax
        self.order_type = order_type
        self.flat_fee = flat_fee

       
    # WE initialise the constructive function above to take common parameters 
    #for the subclasses and creates instance attributes


    def get_total(self):
        """Calculate price."""
        base_price = 5
        
    # We define the method get_total to calculate the total price for orders
    # for self.species in species:

        if self.species == "Christmas melon":
            base_price = 1.5 * base_price
            total = (1 + self.tax) * self.qty * base_price
            return float(total)
        else:
            total = (1 + self.tax) * self.qty * base_price
            return float(total)

        if self.order_type == "international" and self.qty < 10:
            total = (1 + self.tax) * self.qty * base_price + self.flat_fee
            return float(total)



    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    # We define the method mark_shipped that when called sets shipped == true

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, 0.08, "domestic")
    
    # We initialize a subclass and pass class attributes for tax and order_type
    # We also call upon the parent methods and atrributes

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, 
                                                      qty, 
                                                      0.17,
                                                      "international",
                                                      3)
        self.country_code = country_code
       

   
        
        
    # We initialize a subclass and pass class attributes for tax and order_type
    # We also call upon the parent methods and atrributes
    # We add a new attribute country_code which will be asked upon instantiation

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    # When get_country_code methos called returns the country code for the
    #instance    

