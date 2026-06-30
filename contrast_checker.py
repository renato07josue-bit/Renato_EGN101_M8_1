"""
Accessibility Color Contrast Checker
Capstone Project - EGN-101

This tool checks whether a text color and background color have enough contrast
to be readable according to common WCAG accessibility guidelines.

Author: Renato Jacinto
"""

import argparse
import csv
import re


def hex_to_rgb(hex_color):
    """
    Convert a hex color like #FFFFFF into an RGB tuple.
    Example: #FFFFFF -> (255, 255, 255)
    """
    hex_color = hex_color.strip()

    if hex_color.startswith("#"):
        hex_color = hex_color[1:]

    if not re.fullmatch(r"[0-9a-fA-F]{6}", hex_color):
        raise ValueError(f"Invalid color format: {hex_color}. Use format like #FFFFFF.")

    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    return red, green, blue


def srgb_to_linear(value):
    """
    Convert an sRGB color value to a linear value.
    This is part of the WCAG contrast ratio formula.
    """
    value = value / 255

    if value <= 0.03928:
        return value / 12.92

    return ((value + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb):
    """
    Calculate relative luminance.
    Human vision is more sensitive to green than red or blue,
    so the formula gives green more weight.
    """
    red, green, blue = rgb

    red_linear = srgb_to_linear(red)
    green_linear = srgb_to_linear(green)
    blue_linear = srgb_to_linear(blue)

    return (
        0.2126 * red_linear
        + 0.7152 * green_linear
        + 0.0722 * blue_linear
    )


def contrast_ratio(text_color, background_color):
    """
    Calculate the contrast ratio between two colors.
    The result ranges from 1:1 for no contrast to 21:1 for maximum contrast.
    """
    text_rgb = hex_to_rgb(text_color)
    background_rgb = hex_to_rgb(background_color)

    text_luminance = relative_luminance(text_rgb)
    background_luminance = relative_luminance(background_rgb)

    lighter = max(text_luminance, background_luminance)
    darker = min(text_luminance, background_luminance)

    return (lighter + 0.05) / (darker + 0.05)


def check_accessibility(ratio):
    """
    Check the contrast ratio against common WCAG accessibility levels.
    """
    results = {
        "AA Normal Text": ratio >= 4.5,
        "AAA Normal Text": ratio >= 7.0,
        "AA Large Text": ratio >= 3.0,
        "AAA Large Text": ratio >= 4.5,
        "UI Graphics": ratio >= 3.0,
    }

    return results


def print_result(name, text_color, background_color):
    """
    Print the result for one color pair.
    """
    ratio = contrast_ratio(text_color, background_color)
    checks = check_accessibility(ratio)

    print("=" * 60)
    print(f"Color Pair: {name}")
    print(f"Text Color: {text_color}")
    print(f"Background Color: {background_color}")
    print(f"Contrast Ratio: {ratio:.2f}:1")
    print()

    for rule, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"{rule}: {status}")

    print()

    if ratio >= 4.5:
        print("Conclusion: This color pair is readable for normal text.")
    else:
        print("Conclusion: This color pair may be difficult to read for some users.")

    print("=" * 60)
    print()


def analyze_csv(file_path):
    """
    Analyze multiple color pairs from a CSV file.
    The CSV must have these columns:
    name,text_color,background_color
    """
    with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        required_columns = {"name", "text_color", "background_color"}

        if not required_columns.issubset(reader.fieldnames):
            raise ValueError(
                "CSV must include these columns: name, text_color, background_color"
            )

        for row in reader:
            print_result(
                row["name"],
                row["text_color"],
                row["background_color"]
            )


def run_demo():
    """
    Run built-in examples if the user does not provide custom input.
    """
    examples = [
        ("Black text on white background", "#000000", "#FFFFFF"),
        ("Light gray text on white background", "#CCCCCC", "#FFFFFF"),
        ("Blue text on white background", "#0066CC", "#FFFFFF"),
        ("Red text on dark background", "#FF0000", "#222222"),
        ("White text on teal background", "#FFFFFF", "#26C0BB"),
    ]

    print("Running demo color pairs...\n")

    for name, text_color, background_color in examples:
        print_result(name, text_color, background_color)


def main():
    parser = argparse.ArgumentParser(
        description="Check color contrast accessibility for text and background colors."
    )

    parser.add_argument(
        "--text",
        help="Text color in hex format, example: #000000"
    )

    parser.add_argument(
        "--background",
        help="Background color in hex format, example: #FFFFFF"
    )

    parser.add_argument(
        "--csv",
        help="CSV file with columns: name,text_color,background_color"
    )

    args = parser.parse_args()

    try:
        if args.csv:
            analyze_csv(args.csv)
        elif args.text and args.background:
            print_result("Custom Color Pair", args.text, args.background)
        else:
            run_demo()

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
