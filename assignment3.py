def calculate_rewards(total_expenses):
    if 100 < total_expenses < 200:
        return total_expenses, "Bronze"
    elif 200 < total_expenses < 500:
        return total_expenses, "Silver"
    elif total_expenses > 500:
     return total_expenses, "Gold"
    return None

def process_customer_data(file_name):
    with open(
            file_name,
            "r") as file:
        expenses_report = {}
        for line in file:
            name, amount = line.split(",")
            amount = int(amount.strip())
            expenses_report[name] = calculate_rewards(amount)
    return expenses_report
