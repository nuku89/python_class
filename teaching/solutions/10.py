# Remove all falsy values from a list.
def bouncer(array):
    output = []
    for item in array:
        if item:
            output.append(item)
    return output

print(bouncer([(), 7, "ate", "", False, 9, 0]))
# should return [7, "ate", 9]
