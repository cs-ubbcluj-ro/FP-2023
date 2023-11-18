# Ujfalusi Abel
def check_play_cmd_params(parameters: str):
    elems = parameters.split(" ")
    if len(elems) != 2:
        raise ValueError("Incorrect number of parameters!")

    is_digit = elems[0].isdigit() and elems[1].isdigit()

    if not is_digit:
        raise ValueError("Incorrect parameters - should be numbers!")

    return int(elems[0]), int(elems[1])
