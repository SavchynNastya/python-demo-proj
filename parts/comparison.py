def func():
    print("\nCOMPARISON")
    fl: float = 3.9
    i: int = 3
    s1: str = "website"
    s2: str = "ecommerce"

    print("fl < i = ", fl < i)
    print("fl > i = ", fl > i)
    print("fl <= i = ", fl <= i)
    print("fl >= i = ", fl >= i)
    print("fl == i = ", fl == i)
    print("s1 == s2 = ", s1 == s2)

    s2 = "website"
    print("(s2 value changed to s1) s1 == s2 = ", s1 == s2)
