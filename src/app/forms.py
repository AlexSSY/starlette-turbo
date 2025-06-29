def min_len_validator(minimum=1):

    def validator(name, value):
        if len(value) < minimum:
            return "too short"
        
    return validator


def unique_validator(get_session_callback):

    def validator(name, value):
        pass # ! implement

    return validator


class SignupForm:
    username = {
        "type": "text",
        "validators": [
            min_len_validator(),
        ]
    }