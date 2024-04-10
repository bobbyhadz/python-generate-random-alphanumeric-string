# Generate a random alphanumeric string in Python

import random
import string


def random_alphanumeric_string(length):
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=length
        )
    )


print(random_alphanumeric_string(10))  # 👉️ daJVz1oSjG
print(random_alphanumeric_string(15))  # 👉️ JQ7e5h9AvEjRNSy