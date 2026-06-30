# Accessibility Color Contrast Checker

## Project Overview

This capstone project is about digital accessibility. I built a small Python tool that checks whether a text color and background color have enough contrast to be readable.

Many websites and apps use colors that look nice visually but are difficult to read for users with low vision, color blindness, or other visual accessibility needs. This project demonstrates how a technical design choice, such as choosing colors, can create a real social and ethical issue.

The tool calculates the contrast ratio between two colors and reports whether the color pair passes or fails common accessibility guidelines.

## Topic Category

Accessibility

## Social and Ethical Question

Who gets excluded when digital products are not designed with accessibility in mind?

This project connects to the idea that engineers and designers have a responsibility to build technology that can be used by as many people as possible. Poor color contrast can make websites, apps, and online services harder to use for people with visual impairments.

## What the Artifact Does

The Python program checks the contrast between:

* Text color
* Background color

It accepts colors in hexadecimal format, such as:

* `#000000` for black
* `#FFFFFF` for white
* `#0066CC` for blue

The program calculates the contrast ratio and checks if the result passes accessibility levels for:

* AA normal text
* AAA normal text
* AA large text
* AAA large text
* UI graphics

## Files in This Repository

* `contrast_checker.py` — the main Python program
* `sample_colors.csv` — sample color combinations to test
* `README.md` — project documentation

## How to Run the Program

### Option 1: Run the demo examples

Open a terminal in the project folder and run:

```bash
python contrast_checker.py
```

This will test several built-in color combinations.

### Option 2: Test your own colors

Example:

```bash
python contrast_checker.py --text "#000000" --background "#FFFFFF"
```

This checks black text on a white background.

Another example:

```bash
python contrast_checker.py --text "#CCCCCC" --background "#FFFFFF"
```

This checks light gray text on a white background.

### Option 3: Test multiple colors from the CSV file

Run:

```bash
python contrast_checker.py --csv sample_colors.csv
```

This will analyze every color pair listed in the CSV file.

## What the User Should Look For

The most important result is the contrast ratio.

A higher number means the text is easier to read. A lower number means the text may be difficult to read.

For normal text, a contrast ratio of 4.5:1 or higher is usually considered acceptable for basic accessibility.

Example:

* Black text on white background usually passes.
* Light gray text on white background usually fails.

## Technical Concepts Used

This project connects to several computer engineering concepts from the course:

1. Python programming
   The artifact is built with Python functions, conditionals, error handling, and command-line arguments.

2. Data processing
   The program can read a CSV file and analyze multiple examples of color pairs.

3. Logic
   The program uses if-statements to decide whether a color pair passes or fails accessibility rules.

4. Web and design concepts
   Color contrast is an important part of website and app usability.

5. Ethics in computing
   The project shows how a small technical decision can affect whether people can access digital information.

## Example Output

When running the program, the output looks like this:

```text
============================================================
Color Pair: Black text on white background
Text Color: #000000
Background Color: #FFFFFF
Contrast Ratio: 21.00:1

AA Normal Text: PASS
AAA Normal Text: PASS
AA Large Text: PASS
AAA Large Text: PASS
UI Graphics: PASS

Conclusion: This color pair is readable for normal text.
============================================================
```

## Reflection

This project helped me understand that accessibility is not only a design issue. It is also an engineering and ethical issue. A website can work technically but still fail users if the design makes information hard to read.

As a computer engineering student, I think it is important to test digital products with real users in mind. Tools like this contrast checker can help engineers make better decisions before a product is released.
