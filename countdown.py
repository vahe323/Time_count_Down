import time


def format_time(total_seconds):
    """Convert seconds to HH:MM:SS string."""
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def get_time_from_user():
    """Ask until the user enters a valid HH:MM:SS time."""
    while True:
        text = input("Enter time (HH:MM:SS): ").strip()
        parts = text.split(":")
        if len(parts) == 3 and all(p.isdigit() for p in parts):
            h, m, s = map(int, parts)
            return h * 3600 + m * 60 + s
        print("Invalid input. Use HH:MM:SS, e.g. 00:01:30")


def countdown(total_seconds):
    """Print the remaining time, one line per second."""
    while total_seconds >= 0:
        print(format_time(total_seconds))
        total_seconds -= 1
        if total_seconds >= 0:
            time.sleep(1)
    print("Time's up!")


if __name__ == "__main__":
    countdown(get_time_from_user())
