

[200~# Basic Python Script

  # Print a welcome message
  print("Welcome to my basic Python script!")

  # Perform a simple calculation
  a = 5
  b = 3
  sum = a + b
  print(f"The sum of {a} and {b} is {sum}.")

  # Read user input
  name = input("Enter your name: ")
  print(f"Hello, {name}!")

  # Write to a file
  filename = "output.txt"
  with open(filename, 'w') as file:
      file.write(f"Hello, {name}!\n")
      file.write(f"The sum of {a} and {b} is {sum}.\n")

  print(f"Data has been written to {filename}.")

  # Read from a file
  with open(filename, 'r') as file:
      content = file.read()
      print("File content:")
      print(content)

