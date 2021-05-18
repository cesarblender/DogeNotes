import re


def validatePassword(password):
    if len(password) < 8:
        return {
            "error": "Password is too short.",
        }

    if len(password) > 300:
        return {
            "error": "Password is too long.",
        }

    return True


def checkEmail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if re.search(regex, email):
      return True
    else:
        return {
          "error": "The email is not valid."
        }
