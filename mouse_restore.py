import time
import threading
import pyautogui
import keyboard

saved_position = None
last_position = None
last_move_time = time.time()
lock = threading.Lock()

# Thread to monitor mouse stillness
def monitor_stillness():
    global saved_position, last_position, last_move_time
    while True:
        pos = pyautogui.position()
        if pos != last_position:
            last_move_time = time.time()
            last_position = pos
        if time.time() - last_move_time >= 1:
            if saved_position != pos:
                saved_position = pos
                print(f"Saved position: {saved_position}")
        time.sleep(0.05)

def restore_position():
    global saved_position, last_move_time
    print("Hotkey pressed!")
    if saved_position:
        print(f"Restoring position: {saved_position}")
        pyautogui.moveTo(saved_position)
        last_move_time = time.time()
    else:
        print("No position saved yet.")

def main():
    print("App running. Move mouse, wait 1 second, then press Ctrl+Alt+R to restore position.")
    threading.Thread(target=monitor_stillness, daemon=True).start()
    keyboard.add_hotkey('ctrl+alt+r', restore_position)
    keyboard.wait()

if __name__ == "__main__":
    main()
