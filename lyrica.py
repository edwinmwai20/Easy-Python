import sys
from rich import print
from time import sleep


def lyrica():
    
    lines = [
        ("I got my head out the sunroof", 0.09),
        ("I'm blasting our favourite tunes", 0.09),
        ("I only got one thing on my mind", 0.09),
        ("You got me stuck on the thought of you", 0.09),
        ("You're making me feel brand new", 0.09),
        ("You're more than the sunshine in my eyes", 0.09)
    ]
    
    # Pause durations between each line (in seconds)
    line_delays = [0.5, 0.5, 0.6, 0.5, 0.5, 1.0]

    for i, (text, char_delay) in enumerate(lines):
        for char in text:
            # We use sys.stdout.write for character-by-character control
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(char_delay)
        
        print("") # Move to next line
        sleep(line_delays[i])

if __name__ == "__main__":
    lyrica()