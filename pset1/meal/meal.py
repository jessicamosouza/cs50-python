def main():
    time = input('What time is it? ')
    print(convert(time))

def convert(time):
    hours, minutes = time.split(":")
    time_converted = int(hours) + int(minutes)/60

    if time_converted >= 7.0 and time_converted <= 8.0:
        return "breakfast time"
    elif time_converted >= 12.0 and time_converted <= 13.0:
        return "lunch time"
    elif time_converted >= 18.0 and time_converted <= 19.0:
        return "dinner time"

if __name__ == "__main__":
    main()
