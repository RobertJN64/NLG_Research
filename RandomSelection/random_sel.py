import random

with open("teachers.txt") as f:
    lines = [line.strip() for line in f.readlines()]

n = int(input("Enter selection number: "))
email_list = []
for i in range(0, n):
    l = random.choice(lines)
    lines.remove(l)

    l = l.split(" ")
    name = l[0] + ' ' + l[1]
    email = l[2].lower()
    dept = ' '.join(l[3:])

    print(name + " " + dept + " (" + email + ")")
    email_list.append(email)

print()
print("Emails: ")
print(" ".join(email_list))
