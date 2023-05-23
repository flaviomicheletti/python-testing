import re


def test_sub1():
    # Replacing a specific wordr
    text = "Hello, World! How are you?"

    # Replace "World" with "Universe"
    new_text = re.sub(r"World", "Universe", text)
    assert new_text == "Hello, Universe! How are you?"


def test_sub2():
    # Replacing multiple occurrencesr
    text = "The quick brown fox jumps over the lazy dog."

    # Replace all occurrences of vowels with '*'
    new_text = re.sub(r"[aeiou]", "*", text)
    assert new_text == "Th* q**ck br*wn f*x j*mps *v*r th* l*zy d*g."


def test_sub3():
    #  Using a function as the replacement
    text = "The price is $10.99."

    # Replace the price with its doubled value
    def double_price(match):
        price = float(match.group(0)[1:])
        doubled_price = 2 * price
        return "${:.2f}".format(doubled_price)

    new_text = re.sub(r"\$\d+\.\d+", double_price, text)
    assert new_text == "The price is $21.98."


