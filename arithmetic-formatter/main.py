# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main

print("Without the second argument:\n")
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print("\n")
print("\n")

print("With the second argument as 'True':\n")
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))


# Run unit tests automatically
main(module='test_module', exit=False)
