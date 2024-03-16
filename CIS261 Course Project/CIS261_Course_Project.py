# Yohan Roberts
# CIS261
# Course Project Phase 1

import sys

employees = []

def input_employee_name():
    return input("Enter employee name (or type 'End' to finish): ")

def input_hours():
        return float(input("Enter total hours worked: "))

def input_hourly_rate():
            return float(input("Enter hourly rate: "))

def input_tax_rate():
        return float(input("Enter income tax rate (as a percentage): ")) / 100

def calculate_payroll(hours, hourly_rate, tax_rate):
        gross_pay = hours * hourly_rate
        income_tax = gross_pay * tax_rate
        net_pay = gross_pay - income_tax
        return gross_pay, income_tax, net_pay

while True:
        name = input_employee_name()
        if name.lower() == "end":
            break
        hours = input_hours()
        hourly_rate = input_hourly_rate()
        tax_rate = input_tax_rate()
        gross_pay, income_tax, net_pay = calculate_payroll(hours, hourly_rate, tax_rate)
        
employees.append({
            "hours": hours,
            "gross_pay": gross_pay,
            "income_tax": income_tax,
            "net_pay": net_pay
})

display_employee_details(name, hours, hourly_rate, gross_pay, tax_rate, income_tax, net_pay)

