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
