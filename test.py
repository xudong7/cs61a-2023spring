def reverse(list):
    if len(list) == 1:
        return list
    else:
        return reverse(list[1:]) + list[0]

print(reverse("hello"))



