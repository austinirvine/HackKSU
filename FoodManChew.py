
print("Choose a food genre:")
print("Asian")
print("Cookies")
print("Pizza")
print("Other")
choice = raw_input("\nSelection: ")

if choice.upper() == "ASIAN":
    execfile("HunamScraper.py")
