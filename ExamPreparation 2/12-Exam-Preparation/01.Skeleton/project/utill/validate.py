def __validate_empty_string(value, err_message):
    if not isinstance(value, str) or len(value) < 1:
        raise ValueError(err_message)


def __validate_min_number(value, err_message, num):
    if not isinstance(value, int) or value < num:
        raise ValueError(err_message)

def __validate_max_number(value,err_message, num):
    if not isinstance(value, int) or value > num:
        raise ValueError(err_message)

