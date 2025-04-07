import json
import os

# Load translations from the JSON file
def load_translations():
    if not os.path.exists("translations.json"):
        return {}  # Return an empty dictionary if file doesn't exist
    with open("translations.json", "r", encoding="utf-8") as file:
        return json.load(file)  # Load and return JSON data

# Save translations to the JSON file
def save_translations(translations):
    with open("translations.json", "w", encoding="utf-8") as file:
        json.dump(translations, file, ensure_ascii=False, indent=4)  # Save JSON with proper formatting

# Display the menu options to the user
def show_menu():
    print("\n--- Phrase Translator ---")
    print("1. Translate a phrase")
    print("2. Add a new translation")
    print("3. Show all translations")
    print("4. Exit")
    print("5. Edit a translation")
    print("6. Search for a translation")

# Translate a given English phrase
def translate_phrase(phrase, translations):
    return translations.get(phrase, "Phrase not found.")  # Return translation or default message

# Main function to run the translator program
def main():
    translations = load_translations()  # Load existing translations

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Translate a phrase
            phrase = input("Enter the English phrase: ")
            translation = translations.get(phrase)
            if translation:
                print("Translation:", translation)
            else:
                print("Sorry, translation not found.")

        elif choice == "2":
            # Add a new translation
            eng = input("Enter the English phrase: ")
            trans = input("Enter the translated phrase: ")
            translations[eng] = trans
            save_translations(translations)
            print("Translation added successfully!")

        elif choice == "3":
            # Show all translations
            print("\n--- All Translations ---")
            for eng, trans in translations.items():
                print(f"{eng} => {trans}")

        elif choice == "4":
            # Exit the program
            print("Goodbye!")
            break

        elif choice == "5":
            # Edit an existing translation
            english_phrase = input("Enter the English phrase to edit: ")
            if english_phrase in translations:
                new_translation = input(f"Enter the new translation for '{english_phrase}': ")
                translations[english_phrase] = new_translation
                save_translations(translations)
                print(f"Translation updated: {english_phrase} -> {new_translation}")
            else:
                print("Phrase not found.")

        elif choice == "6":
            # Search for a translation
            phrase_to_search = input("Enter the phrase you want to search for: ")
            print(f"Search result: {translate_phrase(phrase_to_search, translations)}")

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Start the program
if __name__ == "__main__":
    main()
