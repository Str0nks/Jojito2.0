"""
"" Load config and create bot instance
"""

def get_token():
    with open("secret", "r") as file: 
        secret = file.readlines()[0]
        return secret

    return ""
