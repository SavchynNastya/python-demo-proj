def func():
    print("\nSTRINGS")
    a = """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua."""
    print(a)

    a = "Django"
    print("Third character in 'Django' - ", a[3])
    print("Length of 'Django' - ", len(a))

    # foreach
    for ch in "Web-developer":
        print(f"{ch} ")

    string = "There are many ways to learn Python fast"
    print(f"Check if a string contains substring - {'are' in string}")

    print(f"Get the part pf the string you need - slice it: {a[1:3]}, {a[:4]}, {a[1:]}")
    print(f"Negative index - {a[-3]}")
    print(a.upper(), " ", a.lower(), " ", a.replace('D', 'F'))

    a = "  cool, but too much spaces   "
    print(a)
    a = a.strip()
    print(a)

    # explode
    print("Splitting by a character ", a.split(','))
    print("Splitting by a character + maxsplit ", a.split(" ", 4))

    # implode
    joined_str = ' '.join(['word1', 'word2', 'word3'])
    print(joined_str)
    joined_str = " - ".join(map(str, ["str1", 123, "str2"]))
    print(joined_str)

    a = "Nastya"
    b = "Savchyn"
    c = a + " " + b
    print(c)
    print(c.islower(), " ", c.isupper())
    print(c.startswith('N'))


