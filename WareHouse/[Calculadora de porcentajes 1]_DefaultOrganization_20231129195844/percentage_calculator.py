def calculate_percentage(value, percentage):
    try:
        return value * (percentage / 100)
    except ZeroDivisionError:
        return None