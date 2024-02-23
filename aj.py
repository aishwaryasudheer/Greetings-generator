def generate_greeting(first_name, last_name):
    if len(first_name) > 10 or len(last_name) > 10:
        return "Error: First and last names must be 10 characters or less."
    else:
        greeting = f"Hello, {first_name.capitalize()} {last_name.capitalize()}! Have a great day!"
        return greeting

def main():
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name: ")
    greeting_message = generate_greeting(first_name,last_name)
    print(greeting_message)

if _name_ == "_main_":
    main()
