"""
Outdated

In a file called outdated.py, implement a program that prompts the user for a
date, anno Domini, in month-day-year order, formatted like 9/8/1636 or
September 8, 1636. Then output that same date in YYYY-MM-DD format. If the
user's input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a
month has 28, 29, 30, or 31 days.
"""

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

if __name__ == "__main__":
    
    while True:
        date = input("Date: ").strip().lower()
        
        try:
            month, day, year = date.split('/')
        except ValueError:        
            try:
                month, day, year = date.split(' ')
            except ValueError:
                continue
                
        # Check valid day
        day_num = int(day.removesuffix(','))
        if day_num <= 0 or day_num > 31:
            continue
        
        # Check valid month
        try:
            month_num = months[month.lower().title()]
        except KeyError:
            month_num = int(month)
        
        if month_num <= 0 or month_num > 12:
            continue
        
        # Check valid year
        try:
            year_num = int(year)
        except TypeError:
            continue
        
        break
        
    print(f"{year_num}-{month_num:>02}-{day_num:>02}")