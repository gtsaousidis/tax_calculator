def calculate_tax(annual_net):
    tax = 0
    
    if annual_net <= 10000:
        tax = annual_net * 0.09
    elif annual_net <= 20000:
        tax = 10000 * 0.09 + (annual_net - 10000) * 0.22
    elif annual_net <= 30000:
        tax = 10000 * 0.09 + 10000 * 0.22 + (annual_net - 20000) * 0.28
    elif annual_net <= 40000:
        tax = 10000 * 0.09 + 10000 * 0.22 + 10000 * 0.28 + (annual_net - 30000) * 0.36
    else:
        tax = 10000 * 0.09 + 10000 * 0.22 + 10000 * 0.28 + 10000 * 0.36 + (annual_net - 40000) * 0.44
    
    return tax

def calculate_health_insurance(category):
    monthly_costs = {
        1: 230.25,
        2: 276.31,
        3: 331.13,
        4: 398.02,
        5: 476.96,
        6: 620.60,
        7: 138.15
    }
    monthly_cost = monthly_costs.get(category, 0)
    return monthly_cost * 12

def main():
    try:
        # Input the annual net income
        annual_net = float(input("Enter your annual net income: "))
        tax = calculate_tax(annual_net)
        
        # Select the health insurance category
        print("\nSelect your category for health insurance:")
        print("1. Category 1\n2. Category 2\n3. Category 3\n4. Category 4\n5. Category 5\n6. Category 6\n7. Special Category")
        category = int(input("Enter your category (1-7): "))
        
        if category not in range(1, 8):
            print("Invalid category. Please enter a number between 1 and 7.")
            return
        
        # Calculate the health insurance and display results
        health_insurance = calculate_health_insurance(category)
        total_deductions = tax + health_insurance
        final_income = annual_net - total_deductions
        
        print(f"\nThe annual tax for an income of {annual_net} is: {tax:.2f}")
        print(f"The annual health insurance cost for category {category} is: {health_insurance:.2f}")
        print(f"\nTotal deductions (tax + insurance): {total_deductions:.2f}")
        print(f"Final net income after deductions: {final_income:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()
