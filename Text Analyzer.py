from collections import Counter
import re


def analyze_text():

    print("=" * 50)
    print("          📝 TEXT ANALYZER")
    print("=" * 50)

    text = input("\nEnter your text:\n").strip()

    if not text:
        print("❌ Please enter some text.")
        return

    # Words
    words = re.findall(r"\b[\w']+\b", text)

    # Sentences
    sentences = re.findall(r"[.!?]+", text)

    # Word count
    word_count = len(words)

    # Character count
    character_count = len(text)

    # Characters without spaces
    characters_without_spaces = len(
        text.replace(" ", "")
    )

    # Longest word
    longest_word = max(words, key=len)

    # Word frequency
    word_frequency = Counter(
        word.lower() for word in words
    )

    print("\n" + "=" * 50)
    print("              📊 TEXT ANALYSIS")
    print("=" * 50)

    print(f"📝 Words                  : {word_count}")
    print(f"🔤 Characters             : {character_count}")
    print(
        f"🔡 Characters without spaces: "
        f"{characters_without_spaces}"
    )
    print(f"📌 Sentences              : {len(sentences)}")
    print(f"📏 Longest Word           : {longest_word}")

    print("\n🔝 Most Frequent Words:")

    for word, count in word_frequency.most_common(5):
        print(f"   {word} → {count} time(s)")


analyze_text()