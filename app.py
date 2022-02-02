import inquirer
from os import system
from tabulate import tabulate
from utils.utils import loop_items, notify_user_toast
from utils.input import validate_input

def main():
    all_initials = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print("Welcome to The BT Phone Book Parser")
    
    questions = [
        inquirer.Text('postcode', message="Enter postcode", validate=validate_input),
        inquirer.Text('street', message="Enter street name (optional)", default='', validate=validate_input),
        inquirer.List('format', message="Select search format", choices=[
            'default',
            'advanced'
        ],
        default='default')
    ]

    results = inquirer.prompt(questions)
    # print(results)
    # { 'postcode': 'AB11 2CD', 'street': '', 'format': 'default' }
    
    res = loop_items(all_initials, results["postcode"].lower(), results["street"].lower(), results["format"])
    # print(res)
    results_length = len(res)
    results_msg = ""
    if results_length > 0:
        results_msg = f"You have {results_length} results!"
    else:
        results_msg = "You do not have any results. Check the postcode and street name are spelt correctly."

    if results_length > 0:

        # Clear Console
        try:
            system("cls")
        except:
            system("clear")
        print("\n" * 2)
        
        # Add Table Headers
        res.insert(0, ['Name', 'Phone number', 'Address'])

        print(tabulate([["Search Query", "Postcode", "Street Name"], ["#", results["postcode"], results["street"]]], headers="firstrow"))
        print("\n" * 2)

        # Generate & Print Table
        print(tabulate(res, headers="firstrow", tablefmt="github"))

        notify_user_toast("Search Results Returned", results_msg, 10)
    else:
        print("No Results Found\n")
        print(results_msg)

        notify_user_toast("No Search Results", results_msg, 10)

if __name__ == "__main__":
    main()
