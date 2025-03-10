while True:

    def calculate_loan_eligibility(status, loan_type, loan_amount_requested, salary=0, tenure_years=0, asset_value=0,
                                   has_guarantor=False, monthly_income=0, business_years=0):
        """
        Determine the loan amount based on employment type and check if the requested loan amount is eligible.
        """

        # Loan Type and Tenure Restrictions
        loan_type_multipliers = {
            "personal loan": 5,  # Max multiplier for personal loan
            "home loan": 20,  # Max multiplier for home loan
            "car loan": 10,  # Max multiplier for car loan
            "business loan": 15  # Max multiplier for business loan
        }

        if loan_type not in loan_type_multipliers:
            return {
                "status": "Error",
                "message": "Invalid loan type selected."
            }

        if status.lower() == "employed":
            if salary < 10000:
                return {
                    "status": "Rejected",
                    "loan_amount": 0,
                    "max_emi": 0,
                    "message": "Minimum salary must be ₹10,000 to qualify for a loan."
                }

            # Loan Calculation Based on Salary
            multiplier = loan_type_multipliers[loan_type]
            max_emi = 0.4 * salary  # Max EMI is 40% of salary
            loan_amount = salary * multiplier * tenure_years

        elif status.lower() == "self-employed":
            if business_years < 1:
                return {
                    "status": "Rejected",
                    "loan_amount": 0,
                    "max_emi": 0,
                    "message": "Business must be at least 1 year old to qualify for a loan."
                }

            multiplier = loan_type_multipliers[loan_type]
            max_emi = 0.5 * monthly_income  # Max EMI is 50% of self-employed income
            loan_amount = monthly_income * multiplier * tenure_years

        else:
            return {
                "status": "Error",
                "message": "Invalid employment status entered. Choose 'employed' or 'self-employed'."
            }

        # Check if requested loan amount is within eligible range
        if loan_amount_requested > loan_amount:
            return {
                "status": "Rejected",
                "loan_amount": loan_amount,
                "max_emi": max_emi,
                "message": f"Requested loan amount ₹{loan_amount_requested} exceeds eligibility of ₹{loan_amount}. Apply for a lower amount."
            }
        else:
            return {
                "status": "Approved",
                "loan_amount": round(loan_amount_requested, 2),
                "max_emi": round(max_emi, 2),
                "message": "Your loan is approved. Please submit necessary documents."
            }


    # Available Loan Types
    print("Available Loan Types:")
    print("1. Personal Loan ")
    print("2. Home Loan ")
    print("3. Car Loan ")
    print("4. Business Loan ")
    print("5. Exit")

    loan_type_map = {
        "1": "personal loan",
        "2": "home loan",
        "3": "car loan",
        "4": "business loan"
    }

    loan_choice = input("\nEnter the number corresponding to the loan type you want: ").strip()
    loan_type = loan_type_map.get(loan_choice)

    if not loan_type:
        print("Invalid choice. Please restart the application.")
        exit()

    loan_amount_requested = float(input(f"\nEnter the loan amount you want for {loan_type.capitalize()}: ₹"))

    # Employment Type Options
    print("\nEmployment Status Options:")
    print("1. Employed")
    print("2. Self-Employed")
    print("3. Exit")

    status_choice = input("\nEnter the number corresponding to your employment status: ").strip()

    if status_choice == "1":
        status = "employed"
    elif status_choice == "2":
        status = "self-employed"
    elif status_choice =="3":
        exit()
    else:
        print("Invalid input. Please restart the application.")
        exit()

    # Input Details Based on Employment Status
    if status == "employed":
        salary = float(input("\nEnter your monthly salary: ₹"))
        tenure = int(input("Enter loan tenure (years): "))
        result = calculate_loan_eligibility(status, loan_type, loan_amount_requested, salary=salary, tenure_years=tenure)

    elif status == "self-employed":
        monthly_income = float(input("\nEnter your average monthly income: ₹"))
        business_years = int(input("How many years have you been in business? "))
        tenure = int(input("Enter loan tenure (years): "))
        result = calculate_loan_eligibility(status, loan_type, loan_amount_requested, tenure_years=tenure,
                                            monthly_income=monthly_income, business_years=business_years)

    # Display Results
    print("\nLoan Status:", result["status"])
    print("Eligible Loan Amount: ₹", result["loan_amount"])
    print("Maximum EMI Allowed:", result["max_emi"])
    print("Message:", result["message"])
