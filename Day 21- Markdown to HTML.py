import re


def convert_markdown_to_html(markdown):
    lines = markdown.splitlines()
    html = []

    in_list = False

    for line in lines:

        line = line.strip()

        # Empty line
        if not line:
            if in_list:
                html.append("</ul>")
                in_list = False

            continue

        # Headings
        if line.startswith("### "):
            content = line[4:]
            html.append(f"<h3>{content}</h3>")

        elif line.startswith("## "):
            content = line[3:]
            html.append(f"<h2>{content}</h2>")

        elif line.startswith("# "):
            content = line[2:]
            html.append(f"<h1>{content}</h1>")

        # Bullet list
        elif line.startswith("- "):

            if not in_list:
                html.append("<ul>")
                in_list = True

            content = line[2:]
            html.append(f"<li>{content}</li>")

        # Normal paragraph
        else:

            if in_list:
                html.append("</ul>")
                in_list = False

            html.append(f"<p>{line}</p>")

    if in_list:
        html.append("</ul>")

    result = "\n".join(html)

    # Bold: **text**
    result = re.sub(
        r"\*\*(.*?)\*\*",
        r"<strong>\1</strong>",
        result
    )

    # Italic: *text*
    result = re.sub(
        r"\*(.*?)\*",
        r"<em>\1</em>",
        result
    )

    # Inline code: `code`
    result = re.sub(
        r"`(.*?)`",
        r"<code>\1</code>",
        result
    )

    # Links: [text](url)
    result = re.sub(
        r"\[(.*?)\]\((.*?)\)",
        r'<a href="\2">\1</a>',
        result
    )

    return result


def create_html_file(html_content):

    complete_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Markdown Converted Page</title>
</head>

<body>

{html_content}

</body>
</html>
"""

    with open("output.html", "w", encoding="utf-8") as file:
        file.write(complete_html)

    print("\n✅ HTML file created successfully!")
    print("📄 File: output.html")


def main():

    print("=" * 55)
    print("       📝 MARKDOWN → HTML CONVERTER")
    print("=" * 55)

    print("""
Enter your Markdown text.
Type END on a new line when finished.
""")

    lines = []

    while True:

        line = input()

        if line == "END":
            break

        lines.append(line)

    markdown = "\n".join(lines)

    if not markdown.strip():
        print("❌ No Markdown content entered.")
        return

    html = convert_markdown_to_html(markdown)

    print("\n" + "=" * 55)
    print("              🌐 GENERATED HTML")
    print("=" * 55)

    print(html)

    create_html_file(html)


main()