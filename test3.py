items = ["john", "eli", "ogo"]

index = 0
for item in items:
    print(f"{index }: {item}")

    index += 1

print("Select a number from the list above: ")
selection = int(input())
print(f"You selected {items[selection]}")

