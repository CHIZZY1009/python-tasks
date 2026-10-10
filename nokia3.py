

def open_submenu(title, options):
   
    while True:
        choice = show_menu(title, options)

        if choice == 99:
            return "home"
        elif choice == 0:
            return "back"
        elif choice in options:
            print("\nYou selected:", options[choice])
            input("Press Enter to continue...")
        elif choice == -1:
            continue
        else:
            print("Invalid choice. Try again.")


def phone_book():
    return open_submenu("PHONE BOOK", {
        1: "Search",
        2: "Service Nos.",
        3: "Add name",
        4: "Erase",
        5: "Edit",
        6: "Copy",
        7: "Assign tone",
        8: "Send business card",
        9: "Options",
        10: "Speed dials",
        11: "Voice tags"
    })


def messages():
    return open_submenu("MESSAGES", {
        1: "Write messages",
        2: "Inbox",
        3: "Outbox",
        4: "Picture messages",
        5: "Templates",
        6: "Smileys",
        7: "Message settings",
        8: "Info service",
        9: "Voice mailbox number",
        10: "Service command editor"
    })


def chat():
    return open_submenu("CHAT", {1: "Chat"})


def call_register():
    return open_submenu("CALL REGISTER", {
        1: "Missed calls",
        2: "Received calls",
        3: "Dialed numbers",
        4: "Erase recent call lists",
        5: "Show call duration",
        6: "Show call costs",
        7: "Call cost settings",
        8: "Prepaid credit"
    })


def tones():
    return open_submenu("TONES", {
        1: "Ringing tone",
        2: "Ringing volume",
        3: "Incoming call alert",
        4: "Message alert tone",
        5: "Keypad tones",
        6: "Warning tones",
        7: "Vibrating alert",
        8: "Screen saver"
    })


def settings():
    return open_submenu("SETTINGS", {
        1: "Call settings",
        2: "Phone settings",
        3: "Security settings",
        4: "Restore factory settings"
    })


def call_divert():
    return open_submenu("CALL DIVERT", {1: "Call divert"})


def music():
    return open_submenu("MUSIC", {
        1: "Music Player",
        2: "Radio",
        3: "Recorder",
        4: "Track list"
    })


def games():
    return open_submenu("GAMES", {1: "Games"})


def calculator():
    return open_submenu("CALCULATOR", {1: "Calculator"})


def reminders():
    return open_submenu("REMINDERS", {1: "Reminders"})


def clock():
    return open_submenu("CLOCK", {
        1: "Alarm clock",
        2: "Clock settings",
        3: "Date setting",
        4: "Stopwatch",
        5: "Countdown timer",
        6: "Auto update of date and time"
    })


def profiles():
    return open_submenu("PROFILES", {1: "Profiles"})


def services():
    return open_submenu("SERVICES", {1: "Services"})


def sim_services():
    return open_submenu("SIM SERVICES", {1: "SIM services"})


def main():
   
    menu_functions = {
        1: ("Phone book", phone_book),
        2: ("Messages", messages),
        3: ("Chat", chat),
        4: ("Call register", call_register),
        5: ("Tones", tones),
        6: ("Settings", settings),
        7: ("Call divert", call_divert),
        8: ("Music", music),
        9: ("Games", games),
        10: ("Calculator", calculator),
        11: ("Reminders", reminders),
        12: ("Clock", clock),
        13: ("Profiles", profiles),
        14: ("Services", services),
        15: ("SIM services", sim_services)
    }

    while True:
        choice = show_menu("NOKIA MAIN MENU", {
            number: details[0]
            for number, details in menu_functions.items()
        })

        if choice == 0:
            print("Goodbye!")
            break
        elif choice == 99:
           
            continue
        
