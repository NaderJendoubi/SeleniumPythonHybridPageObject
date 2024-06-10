import random
import string


def generate_random_email():
    # Generate a random length for the username between 7 and 15
    username_length = random.randint(7, 15)

    # Determine the number of digits to insert, ensuring it's between 0 and 5
    num_digits = random.randint(0, min(5, username_length - 1))

    # Generate a random string of letters for the username
    letters_length = username_length - num_digits
    letters = ''.join(random.choices(string.ascii_lowercase, k=letters_length))

    # Generate a random string of digits
    digits = ''.join(random.choices(string.digits, k=num_digits))

    # Combine letters and digits
    username = letters + digits

    # Randomly choose a domain
    domains = ["@gmail.com", "@yahoo.com", "@outlook.com", "@protonmail.com"]
    domain = random.choice(domains)

    return username + domain


random_email = generate_random_email()
print(random_email)


def generate_random_password():
    # Define the length of the password between 10 and 20 characters
    length = random.randint(10, 20)

    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Generate a random password
random_password = generate_random_password()
print(random_password)


def generate_random_phone_number():
    # Dictionary of country codes and corresponding number formats
    country_codes = {
        "USA": "(###) ###-####",
        "UK": "0#### ######",
        "France": "0# ## ## ## ##",
        "Germany": "0### #######",
        # Add more countries and their number formats here
        "Tunisia": "## ### ###"
    }

    # Choose a random country code
    country = random.choice(list(country_codes.keys()))
    number_format = country_codes[country]

    # Generate a random phone number based on the format for the selected country
    phone_number = ''.join(random.choice('0123456789') if char == '#' else char for char in number_format)

    return f"{country}: {phone_number}"


# Generate a random phone number from a random country
random_phone_number = generate_random_phone_number()
print("Randomly generated phone number:", random_phone_number)
