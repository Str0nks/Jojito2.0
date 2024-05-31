"""
"" Load config and create bot instance
"""

def get_token():
    file = open("secret", "r")
    secret = file.readlines()[0]
    return secret
