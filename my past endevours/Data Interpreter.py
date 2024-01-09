import json

keywords = [
    "setup", "install", "uninstall", "update", "upgrade", "configuration", "settings", 
    "computer", "laptop", "smartphone", "tablet", "printer", "PC", "device", "monitor", 
    "screen", "Windows", "Mac", "iOS", "Android", "Linux", "operating system", "OS", 
    "macOS", "browser", "email", "Microsoft Office", "antivirus", "app", "application", 
    "program", "software", "Word", "Excel", "PowerPoint", "Wi-Fi", "internet", "connect", 
    "disconnect", "router", "modem", "network", "LAN", "WLAN", "connection", "password", 
    "security", "antivirus", "firewall", "malware", "phishing", "hack", "encryption", 
    "VPN", "privacy", "error", "crash", "freeze", "slow", "not working", "bug", "issue", 
    "problem", "fault", "malfunction", "photo", "video", "music", "streaming", "YouTube", 
    "Netflix", "media", "image", "song", "playback", "email", "social media", "WhatsApp", 
    "Facebook", "Skype", "messenger", "Instagram", "LinkedIn", "communication", "chat", 
    "file", "folder", "save", "delete", "backup", "restore", "data", "storage", "document", 
    "upload", "download", "troubleshoot", "diagnose", "repair", "recover", "fix", "solution", 
    "resolve", "maintenance", "technical support", "online banking", "shopping online", 
    "digital payment", "e-commerce", "website", "web", "service", "online account", 
    "printer", "scanner", "camera", "USB", "Bluetooth", "external", "hardware", "peripheral", 
    "mouse", "keyboard", "search", "find", "Google", "maps", "navigate", "explorer", 
    "browser", "accessibility", "screen reader", "magnifier", "assistive", "access", 
    "ease of use", "voice control", "GPay", "Paytm", "UPI", "BHIM", "Aadhaar", "IRCTC", 
    "Flipkart", "Amazon India", "OLX", "Quickr", "Zomato", "Swiggy", "Ola", "Uber India", 
    "Hotstar", "Jio", "Airtel", "Vodafone", "Idea", "BSNL", "Tata Sky", "DishTV", "RedBus", 
    "MakeMyTrip", "BookMyShow", "Practo", "CRED", "Myntra", "BigBasket", "Grofers", 
    "Snapdeal", "Gaana", "Saavn", "JioSaavn", "Aarogya Setu", "COWIN", "Digilocker"
]

#this was meant to be for Googles NQ dataset. Didn't work out well enough, not enough high quality tech questions.

output_file_path = r"relevant_questions.txt"
counter = 0

print("Starting the filtering process...")
with open(r"nq.jsonl", "r") as file, \
     open(output_file_path, "w", encoding='utf-8') as output_file:
    
    print("file opened")
    for line in file:
        counter += 1
        if counter % 1000 == 0:
            print(f"Processed {counter} lines...")

        data = json.loads(line)
        question = data['question_text'].lower()  # Convert to lowercase for case-insensitive matching
        if any(keyword in question for keyword in keywords):
            output_file.write(question + '\n')

print(f"Filtering complete. Relevant questions written to {output_file_path}")
