def validate_non_empty_string(value, err_message):
    if value is not str or len(value) < 1:
        raise ValueError(err_message)