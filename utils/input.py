from ukpostcodeutils import validation

def validate_postcode(postcode):
    if not isinstance(postcode, str):
        return False
    postcode = postcode.replace(" ", "")
    if validation.is_valid_postcode(postcode) or validation.is_valid_partial_postcode(postcode):
        return True
    return False


def input_actions(input):
    if not isinstance(input, str):
        return False
    if input.lower() == "quit" or input.lower() == "exit":
        quit()
    elif input.lower() == "restart":
        print("\n\nRestart\n")
        return True
    return True


def validate_input(answers, current):
    error = input_actions(current)
    if not error:
        return False
    if answers == {}:
        if current == "":
            return False
        return validate_postcode(current)
    return True
