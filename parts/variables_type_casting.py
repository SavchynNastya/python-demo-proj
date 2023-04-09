import ctypes


def func():
    print("VARIABLES")
    s = "hello"
    print(f"{s} - type: {type(s)}")
    s = 3
    print(f"{s} - type: {type(s)}")
    s = 16.03
    print(f"{s} - type: {type(s)}")
    s = [1, 2, 3]
    print(f"{s} - type: {type(s)}")
    s = (1, 2, 3)
    print(f"{s} - type: {type(s)}")
    s = range(3)
    print(f"{s} - type: {type(s)}")
    s = {"var1": "value"}
    print(f"{s} - type: {type(s)}")
    s = {"var1", "var2", "var3"}
    print(f"{s} - type: {type(s)}")
    print(list(s))
    s = b"bytes"
    print(f"{s} - type: {type(s)}")
    s = bytearray(4)
    print(f"{s} - type: {type(s)}")
    s = memoryview(bytes(5))
    print(f"{s} - type: {type(s)}")
    s = 1j
    print(f"{s} - type: {type(s)}")
    s = True
    print(f"{s} - type: {type(s)}")
    print(int(s))

    k: str = "immutable type variable"

    print("GETTING VALUE BY ITS ADDRESS")
    number = 25
    print("Value - ", number)
    address_of_number = id(number)
    print("Address of number - ", address_of_number)
    value_by_address = ctypes.cast(address_of_number, ctypes.py_object).value
    print("Value of variable by the address - ", value_by_address)

