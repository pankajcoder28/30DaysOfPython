'''1. Python has the module called statistics and we can use this module to do all
the statistical calculations. However, to learn how to make function and reuse
function let us try to develop a program, which calculates the measure of
central tendency of a sample (mean, median, mode) and measure of
variability (range, variance, standard deviation). In addition to those
measures, find the min, max, count, percentile, and frequency distribution of
the sample. You can create a class called Statistics and create all the
functions that do statistical calculations as methods for the Statistics class.'''

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

from statistics import mean, median, multimode, variance, stdev
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data
        self.sorted_data = sorted(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(mean(self.data))  

    def median(self):
        return median(self.data)

    def mode(self):
        mode_list = multimode(self.data)  
        mode_value = mode_list[0]
        mode_count = self.data.count(mode_value)
        return (mode_value, mode_count)

    def std(self):
        return round(stdev(self.data), 1)

    def var(self):
        return round(variance(self.data), 1)

    def freq_dist(self):
        freq = Counter(self.data)
        total = self.count()
        freq_list = [(round((freq[num] * 100) / total, 1), num) for num in freq]
        return sorted(freq_list, key=lambda x: (-x[0], -x[1]))  

    
    
data = Statistics(ages)

print('Count:', data.count())        
print('Sum: ', data.sum())          
print('Min: ', data.min())          
print('Max: ', data.max())            
print('Range: ', data.range())        
print('Mean: ', data.mean())          
print('Median: ', data.median())      
print('Mode: ', data.mode())          
print('Standard Deviation:', data.std())   
print('Variance: ', data.var())       
print('Frequency Distribution:', data.freq_dist())

#level 2
'''1. Create a class called PersonAccount. It has firstname, lastname, incomes,
expenses properties and it has total_income, total_expense, account_info,
add_income, add_expense and account_balance methods. Incomes is a set
of incomes and its description. The same goes for expenses.'''

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, description, amount):
        self.incomes.append((description, float(amount)))

    def add_expense(self, description, amount):
        self.expenses.append((description, float(amount)))

    def total_income(self):
        return sum(amount for _, amount in self.incomes)

    def total_expense(self):
        return sum(amount for _, amount in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        lines = [
            f"Account Holder: {self.firstname} {self.lastname}",
            f"Total Income: {self.total_income()}",
            f"Total Expense: {self.total_expense()}",
            f"Balance: {self.account_balance()}",
            f"Incomes: {self.incomes}",
            f"Expenses: {self.expenses}",
        ]
        return "\n".join(lines)
    
acc = PersonAccount("Pankaj", "Kumar")

acc.add_income("Salary", 50000)
acc.add_income("Freelance", 8000)
acc.add_expense("Rent", 12000)
acc.add_expense("Food", 6000)
acc.add_expense("Internet", 800)

print("Total Income:", acc.total_income())       
print("Total Expense:", acc.total_expense())     
print("Balance:", acc.account_balance())         
print(acc.account_info())

