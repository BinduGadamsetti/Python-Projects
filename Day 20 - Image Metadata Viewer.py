from PIL import Image
import os


def analyze_image(filename):

    if not os.path.exists(filename):
        print("❌ Image not found.")
        return

    try:
        image = Image.open(filename)

        width, height = image.size

        file_size = os.path.getsize(filename)

        file_size_kb = file_size / 1024

        print("\n" + "=" * 50)
        print("           🖼️ IMAGE INFORMATION")
        print("=" * 50)

        print(f"📁 File Name   : {os.path.basename(filename)}")
        print(f"🖼️ Format      : {image.format}")
        print(f"📐 Width       : {width} px")
        print(f"📏 Height      : {height} px")
        print(f"📊 Color Mode  : {image.mode}")
        print(f"💾 File Size   : {file_size_kb:.2f} KB")

        print(f"🔢 Total Pixels: {width * height:,}")

        if width > height:
            orientation = "Landscape"

        elif height > width:
            orientation = "Portrait"

        else:
            orientation = "Square"

        print(f"📷 Orientation : {orientation}")

        print("=" * 50)

        save_report(
            filename,
            image,
            width,
            height,
            file_size_kb,
            orientation
        )

    except Exception as error:
        print(f"❌ Error: {error}")


def save_report(
    filename,
    image,
    width,
    height,
    file_size_kb,
    orientation
):

    report_name = "image_report.txt"

    with open(report_name, "w") as file:

        file.write("IMAGE INFORMATION REPORT\n")
        file.write("=" * 35 + "\n")

        file.write(
            f"File Name: {os.path.basename(filename)}\n"
        )

        file.write(f"Format: {image.format}\n")
        file.write(f"Width: {width} px\n")
        file.write(f"Height: {height} px\n")
        file.write(f"Color Mode: {image.mode}\n")
        file.write(f"File Size: {file_size_kb:.2f} KB\n")
        file.write(f"Orientation: {orientation}\n")

    print("\n📄 Report saved as image_report.txt")


def main():

    print("=" * 50)
    print("          🖼️ IMAGE METADATA VIEWER")
    print("=" * 50)

    filename = input(
        "\nEnter image path: "
    ).strip()

    analyze_image(filename)


main()