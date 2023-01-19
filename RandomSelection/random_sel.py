import random

with open("teachers.txt") as f:
    lines = [line.strip() for line in f.readlines()]

with open("sel.txt") as f:
    ban_list = [line.strip() for line in f.readlines()]

n = int(input("Enter selection number: "))
email_list = []
i = 0
while i < n:
    l = random.choice(lines)
    lines.remove(l)

    l = l.split(" ")
    name = l[0] + ' ' + l[1]
    email = l[2].lower()
    dept = ' '.join(l[3:])

    if email in ban_list:
        continue

    if '@ccs.k12.in.us' not in email:
        print("Error:", email)

    print(name + " " + dept + " (" + email + ")")
    email_list.append(email)
    i += 1

print()
print("Emails: ")
print(" ".join(email_list))

if input("Add to sel? y/n ") == 'y':
    with open("sel.txt", 'a') as f:
        f.write("\n".join(email_list))
        f.write("\n")