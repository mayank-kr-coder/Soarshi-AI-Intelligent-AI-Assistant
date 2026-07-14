import webbrowser
import datetime
import pyjokes
import os

def execute_command(command):

    command = command.lower()


    if "open youtube" in command:

       return {
        "response": "Opening YouTube",
        "action": "open_url",
        "url": "https://youtube.com"
    }


    elif "open google" in command:

        return {
            "response": "Opening Google",
            "action": "open_url",
            "url": "https://google.com"
        }
        


    elif "open chatgpt" in command:

        return {
            "response": "Opening ChatGPT",
            "action": "open_url",
            "url": "https://chatgpt.com"
        }

    elif "open github" in command:

        return {
        "response": "Opening GitHub",
        "action": "open_url",
        "url": "https://github.com"
    }


    elif "open linkedin" in command:

        return {
        "response": "Opening LinkedIn",
        "action": "open_url",
        "url": "https://linkedin.com"
        }


    elif "open gmail" in command:

        return {
            "response": "Opening Gmail",
            "action": "open_url",
            "url": "https://mail.google.com"
        }


    elif "open instagram" in command:

        return {
            "response": "Opening Instagram",
            "action": "open_url",
            "url": "https://instagram.com"
        }


    elif "open facebook" in command:

        return {
            "response": "Opening Facebook",
            "action": "open_url",
            "url": "https://facebook.com"
        }


    elif "open twitter" in command or "open x" in command:

        return {
            "response": "Opening X",
            "action": "open_url",
            "url": "https://x.com"
        }


    elif "open whatsapp" in command:

        return {
            "response": "Opening WhatsApp",
            "action": "open_url",
            "url": "https://web.whatsapp.com"
        }


    elif "open stack overflow" in command:

        return {
            "response": "Opening Stack Overflow",
            "action": "open_url",
            "url": "https://stackoverflow.com"
        }

    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"


    elif "date" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today's date is {today}"


    elif "joke" in command:

        return pyjokes.get_joke()


    elif "open chrome" in command or "open google chrome" in command or "open browser" in command:

        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        return "Opening Chrome"


    elif "open notepad" in command or "open document" in command or "open notebook" in command:

        os.system("notepad")
        return "Opening Notepad"


    elif "open calculator" in command or "open calc" in command:

        os.system("calc")
        return "Opening Calculator"
    
    elif "open file manager" in command or "file manager" in command or "open files" in command:
        os.system("explorer")
        return "Opening File Manager"
    
    elif "open command prompt" in command or "open cmd" in command:
        os.system("start cmd")
        return "Opening Command Prompt"
    
    elif "open windows " in command or "open settings" in command or "open control panel" in command:
        os.system("start ms-settings:")
        return "Opening Windows Settings"


    elif "open camera" in command or "open webcam" in command:

        os.system("start microsoft.windows.camera:")
        return "Opening Camera"


    elif "search google" in command:

        query = command.replace("search google", "").strip()

        return {
            "response": f"Searching Google for {query}",
            "action": "open_url",
            "url": f"https://www.google.com/search?q={query}"
        }

    elif "play" in command:

        import pywhatkit

        song = (
            command
            .replace("play", "")
            .replace("on youtube", "")
            .strip()
        )

        pywhatkit.playonyt(song)

        return f"Playing {song} on YouTube"


    elif "refresh" in command:
        import pyautogui

        pyautogui.press("f5")

        return "Refreshing screen"


    elif "show desktop" in command or "minimize tab" in command:
        import pyautogui

        pyautogui.hotkey("win", "d")

        return "Showing desktop"


    elif "take screenshot" in command or "screenshot" in command:
        import pyautogui
        screenshot = pyautogui.screenshot()

        screenshot.save("screenshot.png")

        return "Screenshot saved successfully"


    elif "lock computer" in command or "lock pc" in command:

        os.system("rundll32.exe user32.dll,LockWorkStation")

        return "Locking computer"


    return False









