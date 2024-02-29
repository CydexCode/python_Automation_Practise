import pyautogui
import time

def main():
    # Open Notepad
    pyautogui.hotkey('winleft')
    time.sleep(1)  # Add a delay to make sure the start menu is open
    pyautogui.write('Notepad')
    pyautogui.press('enter')
    time.sleep(2)  # Add a delay to allow Notepad to open

    # Type 'hello, Sachi'
    pyautogui.write('hello, Sachi')

    # Type 'I'm gonna surprise you'
    pyautogui.press('enter')  # Move to the next line
    pyautogui.write("I'm gonna surprise you")

    # Close Notepad without saving
    pyautogui.hotkey('ctrl', 'w')  # Close the current window
    time.sleep(1)  # Add a delay for the "Do you want to save changes" dialog
    pyautogui.press('n')  # Press 'No' to discard changes

if __name__ == "__main__":
    main()
