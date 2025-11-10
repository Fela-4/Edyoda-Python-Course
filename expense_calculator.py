# This program is to calculate the expenses by using a dictionary
# Here onwards, I will practice the use of type-hints


def get_expenses():
    dict_temp: dict[str, float] = {}    # here I am initializing the dictionary

    # this function is made to reduce repition in code and is more efficient
    def user_input(key_name: str) -> None:      # this function does not return any value but directly influence the dictionary(dict_temp)
        while True:
            try:
                value: float = float(input(f"Enter {key_name}: "))

                if value <= 0:  # to make sure no negative or zero value is entered
                    print("Enter a positive number!")
                    continue

                dict_temp[f'{key_name}'] = value    # populating the dictionary
                break

            except ValueError:
                print("INVALID INPUT! Enter a number")


    categories: list[str] = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Utilities']     

    for category in categories:     # a list of categories created above is used to call func user_input using loop
        user_input(category)
       
    return dict_temp


def calculate_total(dict: dict[str, float]) -> float:   # function to calculate total expenses and returns the value
    total: float = 0.0
    for v in dict.values():
        total += v
    return total


def analyze_expenses(dict: dict[str, float], total: float) -> dict[str, str]:   # this function is used to calculate the percentage of each category 
    dict_temp = {}

    for category, cost in dict.items():
        expense_percen = str(round((cost / total) * 100, 2))
        expense_percen += '%'

        dict_temp[category] = expense_percen

    return dict_temp


expenses_dict: dict[str, float] = get_expenses()
total: float = calculate_total(expenses_dict)
analyzed_dict: dict[str, float] = analyze_expenses(expenses_dict, total)

combined_dict: dict[str, tuple[float, str]] = {
    key: (expenses_dict[key], analyzed_dict[key]) for key in expenses_dict.keys() & analyzed_dict.keys()    # here i am implementing the use of dictionary comprehension to merge the two diconaries
}                   

formatted_report: str = "\n"    # intiliazing an empty string with a new line to isolate from the user's inputs

# im using a loop and appending the variable to a string in a proper format
for category, expense in combined_dict.items():
    str_line: str = f"{category} -- ${expense[0]} -- {expense[1]}\n"
    formatted_report += str_line


print(f"{formatted_report}\n----- Total Expense- ${total} -----")