def clean_minutely_interval_with_user_input():
    minutely_interval = input("Enter the minutely interval e.g., 1, 5, 15, 30, 60 (press Enter to skip visualization): ")

    if minutely_interval == '':
        print("Skip visualization")
    else:
        minutely_interval = minutely_interval.strip()
        print("Input: minutely interval:", minutely_interval)
        minutely_interval = validate_minutely_interval(minutely_interval)

    return minutely_interval

def validate_minutely_interval(minutely_interval):
    try:
        interval = int(minutely_interval)
        if interval in [1, 5, 15, 30, 60]:
            return interval
        else:
            print("Not pass, validation")
            return None  # Returning None for invalid intervals
    except ValueError:
        print("Invalid input, not a valid integer")
        return None  # Returning None for non-integer input