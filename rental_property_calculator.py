class RentalProperty():
    rental_income = None
    total_expenses = None
    cash_flow = None

    def __init__(self, down_payment, closing_costs, rehab_budget, misc_other):
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc_other = misc_other
    
    def getMonthlyIncome(self, rental_income):
        self.rental_income = rental_income
        return "Monthly income from the property is ${:,.2f}".format(self.rental_income)

    def getMonthlyExpenses(self, tax, insurance, utilities, hoa, maintenance, capex, mortgage):
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self.maintenance = maintenance
        self.capex = capex
        self.mortgage = mortgage
        self.total_expenses = tax + insurance + utilities + hoa + maintenance + capex + mortgage
        return "Monthly expense for the property is ${:,.2f}".format(self.total_expenses)

    def getCashFlow(self):
        if self.rental_income is not None and self.total_expenses is not None:
            self.cash_flow = self.rental_income - self.total_expenses
            return "Your monthly cash flow is ${:,.2f}".format(self.cash_flow)
        else:
            return "Please enter monthly income and/or expenses first!"

    def getROI(self):
        if self.cash_flow is not None:
            total_investment = self.down_payment + self.closing_costs + self.rehab_budget + self.misc_other
            annual_cash_flow = self.cash_flow * 12
            cash_on_cash_roi = (annual_cash_flow / total_investment) * 100
            return "Your cash on cash ROI is {:,.2f}%".format(cash_on_cash_roi)
        else:
            return "Please calculate your cash flow first!"

# Instantiating a new property class with values for down_payment, closing_costs, rehab_budget, misc_other
# property_1 = RentalProperty(40000,3000,7000,0)

# Pass value for rental_income and get total monthly income
# print(property_1.getMonthlyIncome(2000))

# Pass expenses for tax, insurance, utilities, hoa, maintenance, capex, mortgage and get total monthly expenses
# print(property_1.getMonthlyExpenses(150, 100, 50, 0, 75, 100, 750))

# Get cash flow 
# print(property_1.getCashFlow())

# Get cash on cash ROI
# print(property_1.getROI())
        
def convertToIntorFloat(string):
    try:
        return int(string)
    except:
        return float(string)

while True:
    quit = False
    down_payment, closing_costs, rehab_budget, misc_other, rental_income = "", "", "", "", ""
    print('Welcome! Please answer the following questions. You may type "QUIT" to exit anytime')
    while True:
        down_payment = input("Enter the down payment amount (in US Dollars): ")
        if down_payment.lower() != 'quit' and not down_payment.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if down_payment.lower() == 'quit':
        print("You have exited!")
        break

    while True:
        closing_costs = input("Enter the closing cost (in US Dollars): ")
        if closing_costs.lower() != 'quit' and not closing_costs.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if closing_costs.lower() == 'quit':
        print("You have exited!")
        break

    while True:
        rehab_budget = input("Enter the rehab budget (in US Dollars): ")
        if rehab_budget.lower() != 'quit' and not rehab_budget.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if rehab_budget.lower() == 'quit':
        print("You have exited!")
        break
    
    while True:
        misc_other = input("Please enter other miscellaneous expenses (in US Dollars): ")
        if misc_other.lower() != 'quit' and not misc_other.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if misc_other.lower() == 'quit':
        print("You have exited!")
        break
    
    down_payment = convertToIntorFloat(down_payment)
    closing_costs = convertToIntorFloat(closing_costs)
    rehab_budget = convertToIntorFloat(rehab_budget)
    misc_other = convertToIntorFloat(misc_other)
    property_1 = RentalProperty(down_payment,closing_costs,rehab_budget,misc_other)

    print("Thank you!")

    while True:
        rental_income = input("Please enter rental income (in US Dollars): ")
        if rental_income.lower() != 'quit' and not rental_income.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if rental_income.lower() == 'quit':
        print("You have exited!")
        break
    
    rental_income = convertToIntorFloat(rental_income)
    print(property_1.getMonthlyIncome(rental_income))

    tax, insurance, utilities, hoa, maintenance, capex, mortgage = "", "", "", "", "", "", ""

    print("Now please enter the following expenses")

    while True:
        tax = input("Tax (in US Dollars): ")
        if tax.lower() != 'quit' and not tax.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if tax.lower() == 'quit':
        print("You have exited!")
        break

    while True:
        insurance = input("Insurance (in US Dollars): ")
        if insurance.lower() != 'quit' and not insurance.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if insurance.lower() == 'quit':
        print("You have exited!")
        break

    while True:
        utilities = input("Utilities (in US Dollars): ")
        if utilities.lower() != 'quit' and not utilities.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if utilities.lower() == 'quit':
        print("You have exited!")
        break

    while True:
        hoa = input("HOA (in US Dollars): ")
        if hoa.lower() != 'quit' and not hoa.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if hoa.lower() == 'quit':
        print("You have exited!")
        break

    while True:
        maintenance = input("Maintenance (in US Dollars): ")
        if maintenance.lower() != 'quit' and not maintenance.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if maintenance.lower() == 'quit':
        print("You have exited!")
        break

    while True:
        capex = input("Capex (in US Dollars): ")
        if capex.lower() != 'quit' and not capex.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if capex.lower() == 'quit':
        print("You have exited!")
        break

    while True:
        mortgage = input("Mortgage (in US Dollars): ")
        if mortgage.lower() != 'quit' and not mortgage.replace(".", "").isnumeric():
            print("Please enter a valid amount")
        else:
            break
    if mortgage.lower() == 'quit':
        print("You have exited!")
        break

    tax = convertToIntorFloat(tax)
    insurance = convertToIntorFloat(insurance)
    utilities = convertToIntorFloat(utilities)
    hoa = convertToIntorFloat(hoa)
    maintenance = convertToIntorFloat(maintenance)
    capex = convertToIntorFloat(capex)
    mortgage = convertToIntorFloat(mortgage)
    print(property_1.getMonthlyExpenses(tax, insurance, utilities, hoa, maintenance, capex, mortgage))
    print(property_1.getCashFlow())
    print(property_1.getROI())
    break