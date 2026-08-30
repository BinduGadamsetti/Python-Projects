import json
import random
import string
import os

FILE = "urls.json"


def load_urls():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}

    return {}


def save_urls(urls):
    with open(FILE, "w") as file:
        json.dump(urls, file, indent=4)


def generate_code(urls):
    characters = string.ascii_letters + string.digits

    while True:
        code = ''.join(random.choices(characters, k=6))

        if code not in urls:
            return code


def shorten_url(urls):

    url = input("\nEnter long URL: ").strip()

    if not url:
        print("❌ URL cannot be empty.")
        return

    if not url.startswith(("http://", "https://")):
        print("⚠️ Adding https:// automatically.")
        url = "https://" + url

    code = generate_code(urls)

    urls[code] = url

    save_urls(urls)

    print("\n✅ URL shortened!")
    print(f"🔗 Short code : {code}")
    print(f"🌐 Original   : {url}")


def open_url(urls):

    code = input("\nEnter short code: ").strip()

    if code in urls:
        print("\n🔍 URL FOUND")
        print(f"🔗 Code     : {code}")
        print(f"🌐 Original : {urls[code]}")
    else:
        print("❌ Short code not found.")


def show_all(urls):

    if not urls:
        print("\n📭 No shortened URLs yet.")
        return

    print("\n" + "=" * 55)
    print("              🔗 SAVED URLS")
    print("=" * 55)

    for code, url in urls.items():
        print(f"\n🔗 {code}")
        print(f"   {url}")


def main():

    urls = load_urls()

    while True:

        print("\n" + "=" * 50)
        print("             🔗 URL SHORTENER")
        print("=" * 50)

        print("""
1. 🔗 Shorten URL
2. 🔍 Find Original URL
3. 📋 View All URLs
4. 🚪 Exit
""")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            shorten_url(urls)

        elif choice == "2":
            open_url(urls)

        elif choice == "3":
            show_all(urls)

        elif choice == "4":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


main()