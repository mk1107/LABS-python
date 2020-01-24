'''Create a 8 character alphanumeric string random
password generator.'''

import string
import random

print(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(8)))