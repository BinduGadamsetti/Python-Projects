from datetime import datetime
import time


def show_clock():
    print("=" * 45)
    print("          🕐 SMART DIGITAL CLOCK")
    print("=" * 45)

    while True:
        now = datetime.now()

        # Get date, day and time
        day = now.strftime("%A")
        date = now.strftime("%d-%m-%Y")
        current_time = now.strftime("%I:%M:%S %p")

        # Display everything
        print(
            f"\r📅 Date: {date}  |  "
            f"📆 Day: {day}  |  "
            f"⏰ Time: {current_time}",
            end="",
            flush=True
        )

        time.sleep(1)


try:
    show_clock()

except KeyboardInterrupt:
    print("\n\n👋 Clock stopped. Have a great day!")