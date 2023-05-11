class Company:
    def __init__(self, name):
        self.name = name
        self.customers = []
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_customers(self):
        return self.customers
    
    def add_customers(self, customer):
        self.customers.append(customer)

    def set_customers(self, customers):
        self.customers = []
        for customer in customers:
            self.customers.append(customer)
        