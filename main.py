from company import Company
from customer import Customer
from membership import Membership
from membership_factory import MembershipFactory
from reg_customer import RegCustomer


def display(company):
    customers = company.get_customers()
    for customer in customers:
        if isinstance(customer, RegCustomer):
            print("Customer Id : ", customer.custId)
            print("Customer Name : ", customer.name)
            print("Customer Email : ", customer.email)
            print("Membership Details : ", customer.getMembership().get_type_of_membership())
            print("Date Reg : ", customer.getDtReg())
        else:
            print("Customer Id : ", customer.custId)
            print("Customer Name : ", customer.name)
            print("Customer Email : ", customer.email)
        print("===========================")


if __name__ == '__main__':
    # create a company
    c1 = Company("Amazon")

    # Create customers
    cus1 = Customer("1", "Shruthi", "shru133@gmail.com")
    cus2 = Customer("2", "Sreeja", "sreeja@gmail.com")

    # Create RegCustomer
    rc1 = RegCustomer("3", "Suraj", "suraj@gmail.com", "20-10-2020")
    rc2 = RegCustomer("4", "Sujay", "sujay@gmail.com", "15-5-2019")

    # Singleton Design Pattern - only one object will be created
    # MembershipFactory is created by call a method getInstance -
    # in which object instantiation is done using singleton pattern
    mem = MembershipFactory.getInstance()

    rc1.setMembership(mem.create("GOLD"))
    rc2.setMembership(mem.create("PLATINUM"))

    customers = [cus1, cus2, rc1, rc2]

    # Add customer and regCustomer to company
    c1.set_customers(customers)

    display(c1)