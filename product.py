class Product:
    '''
    Dummy class using property decorator for getters and setters (BEAUTIFUL)
    '''
    # Class Attribute
    # default_store: str = "Main St Huge Ass Store"

    # Constructor
    def __init__(self, price: int):
        # Instance Attributes- bound to an object
        self.price = price


    # Getter
    @property
    def price(self) -> int:
        return self.__price
    

    # Setter
    @price.setter
    def price(self, price: int) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price
