user_entry = input("Type a list of words separated by a space: ")

words = user_entry.split()

lenth = [len(words) for word in words]

print("Original list:", words)
print("Word's lenths:", lenth)