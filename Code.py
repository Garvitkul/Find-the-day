#!/usr/bin/env python3

def is_leap_year(year):
    """
    Returns True if the given year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


def get_century_offset(year):
    """
    Returns the century offset used in the day calculation formula.
    Based on the century range.
    """
    if 900 <= year <= 999 or 1300 <= year <= 1399 or 1700 <= year <= 1799 or 2100 <= year <= 2199:
        return 5
    elif 1000 <= year <= 1099 or 1400 <= year <= 1499 or 1800 <= year <= 1899 or 2200 <= year <= 2299:
        return 3
    elif 1100 <= year <= 1199 or 1500 <= year <= 1599 or 1900 <= year <= 1999 or 2300 <= year <= 2399:
        return 1
    elif 1200 <= year <= 1299 or 1600 <= year <= 1699 or 2000 <= year <= 2099 or 2400 <= year <= 2499:
        return 0
    else:
        return None  # Invalid century range


def find_day(date, month, year):
    """
    Calculates the day of the week for the given date, month, and year.
    Returns the weekday name or an error message if inputs are invalid.
    """
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Month codes
    month_codes = {
        1: 6,
        2: 2,
        3: 2,
        4: 5,
        5: 7,
        6: 3,
        7: 5,
        8: 1,
        9: 4,
        10: 6,
        11: 2,
        12: 4
    }

    # Adjust for leap year
    if is_leap_year(year):
        month_codes[1] = 5
        month_codes[2] = 1

    # Validate month
    if month not in month_codes:
        return "Invalid month. Please enter a value between 1 and 12."

    # Validate date range roughly (no precise month/day checks here)
    if date < 1 or date > 31:
        return "Invalid date. Please enter a value between 1 and 31."

    # Get century offset
    offset = get_century_offset(year)
    if offset is None:
        return "Year out of supported range (900–2499)."

    # Compute formula
    year_in_century = year % 100
    formula = date + month_codes[month] + year_in_century + (year_in_century // 4) + offset
    day_index = formula % 7

    return days_of_week[day_index]


def main():
    print("=== Day Finder ===")
    try:
        date = int(input("Enter Date (1–31): ").strip())
        month = int(input("Enter Month (1–12): ").strip())
        year = int(input("Enter Year (e.g., 2025): ").strip())

        result = find_day(date, month, year)
        print(f"\nResult: {result}")

    except ValueError:
        print("Error: Please enter valid integers for date, month, and year.")


if __name__ == "__main__":
    main()
