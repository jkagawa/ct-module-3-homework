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
property_1 = RentalProperty(40000,3000,7000,0)

# Pass value for rental_income and get total monthly income
print(property_1.getMonthlyIncome(2000))

# Pass expenses for tax, insurance, utilities, hoa, maintenance, capex, mortgage and get total monthly expenses
print(property_1.getMonthlyExpenses(150, 100, 50, 0, 75, 100, 750))

# Get cash flow 
print(property_1.getCashFlow())

# Get cash on cash ROI
print(property_1.getROI())
