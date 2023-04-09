def func():
    print("\nHASH ARRAYS")
    print("dictionary")
    dictionary = {"name": "Anastasiia", "age": 18}
    print(dictionary, " ", type(dictionary))
    print(dictionary["age"])
    print(dictionary.values())
    print(dictionary.keys())
    dictionary["lastname"] = "Savchyn"
    print(dictionary)
    dictionary["age"] = 20
    dictionary.popitem()
    del dictionary["age"]
    print(dictionary)
    for k, v in dictionary.items():
        print(k, ': ', v)

    print("hash table")
    hash_table = [[] for _ in range(5)]
    print(hash_table)
    hash_table[hash("apple") % 5].append(("apple", 3))
    hash_table[hash("banana") % 5].append(("banana", 6))
    hash_table[hash("orange") % 5].append(("orange", 9))
    print(hash_table)

    key = "apple"
    pair = hash_table[hash(key) % 5]
    print(pair)
    for item in pair:
        if item[0] == key:
            print(item[1])

