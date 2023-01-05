with open("raw.txt") as f:
    lines = [line.strip() for line in f.readlines()]

with open("teachers.txt", "w+") as f:
    for i in range(0, len(lines), 4):
        name = lines[i]
        job = lines[i+1]
        department = lines[i+2]
        email = lines[i+3]
        print("Found", name, "with email", email)
        if job == "Teacher":
            f.write(name + " " + email + " " + department + "\n")