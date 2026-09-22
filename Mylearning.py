# print("Hello, world!")


# favorite_color = input("What is your favorite color? ")
# print("Oh, I love", favorite_color, "too!")


# first = "Hello"
# last = "world"
# message = first + ", " + last + "!"
# print(message)


# name = "Alex"
# print(f"Hello, {name}!")


# # age = input("How old are you? ")
# # print(f"Next year you will be {age + 1}") # Works perfectly!

# #have to save changes in the another variable. otherwise will not get updated one.
# greeting = "hello"
# greeting = greeting.upper() # Saving the new uppercase copy


# colors = ["red", "green", "blue"]

# print(len(colors))        # Output: 3
# colors.append("yellow")   # Adds "yellow" to the end
# print(colors)             # Output: ['red', 'green', 'blue', 'yellow']

# colors.remove("red")      # Removes "red"
# print(colors)             # Output: ['green', 'blue', 'yellow']

# colors[0] = "purple"      # Replaces "green" with "purple"
# print(colors)             # Output: ['purple', 'blue', 'yellow']

# #create dictionary
# user = {
#     "name": "Alex",
#     "age": 25,
#     "email": "alex@example.com"
# }

# print(user["name"])   # Output: Alex
# print(user["age"])    # Output: 25

# user = {"name": "Alex", "age": 25}

# user["email"] = "alex@example.com"   # Add a new key
# user["age"] = 26                     # Update an existing key
# del user["age"]                      # Remove a key

# print("name" in user)                # Output: True

# def greet():
#     print("Hello, world!")

# greet()   # Output: Hello, world!

# def greet(name, greeting):
#     print(f"{greeting}, {name}!")

# greet("Alex", "Hi")   # Output: Hi, Alex!

# def add(a, b):
#     return a + b

# result = add(3, 4)
# print(result)   # Output: 7

# with open(r"C:\Users\Indra.V\Sample.txt", "r") as file:
#     contents = file.read()

# print(contents)

# with open(r"C:\Users\Indra.V\Sample.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(line.strip())

with open(r"C:\Users\Indra.V\Sample.txt", "r") as file:
      for line in file:
        print(line.strip())