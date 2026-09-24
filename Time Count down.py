import time


def get_countdown_seconds():
    """Ask the user for a time in h:m:s format and return it as total seconds."""
    user_input = input("Insert time to count down (h:m:s) ")
    hours, minutes, seconds = user_input.split(":")
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    return total_seconds


def format_time(total_seconds):
    """Convert total seconds into HH:MM:SS format."""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def countdown(total_seconds):
    """Print the countdown, one line per second."""
    while total_seconds >= 0:
        print(format_time(total_seconds))
        time.sleep(1)
        total_seconds -= 1
    print("Time's up!")


def main():
    total_seconds = get_countdown_seconds()
    countdown(total_seconds)


if __name__ == "__main__":
      main()