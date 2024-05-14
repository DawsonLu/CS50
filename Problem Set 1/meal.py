"""
In meal.py, implement a program that prompts the user for a time and outputs 
hether it’s breakfast time, lunch time, or dinner time. If it’s not time for a
meal, don’t output anything at all. Assume that the user’s input will be
formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time
range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or
anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can
be called by main) that converts time, a str in 24-hour format, to the
corresponding number of hours as a float. For instance, given a time like
"7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5
hours).
"""


def main():
    get_input = input("What time is it? ").strip()
    hour = convert(get_input)
    
    if hour >= 7 and hour <= 8:
        print("breakfast time")
        
    elif hour >= 12 and hour <= 13:
        print("lunch time")
        
    elif hour >= 18 and hour <= 19:
        print("dinner time")
        
    return
    
    
def convert(time):
    if time.endswith("p.m."):
        hour, minute = time.removesuffix("p.m.").strip().split(':')
        
        if hour == "12":
            return float(hour) + (float(minute) / 60)
        
        return float(hour) + 12 + (float(minute) / 60)
        
    hour, minute = time.removesuffix("a.m.").strip().split(':')
    return float(hour) + (float(minute) / 60)
    
    
if __name__ == "__main__":
    main()