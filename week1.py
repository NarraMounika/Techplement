import json, os

FILE = "contacts.json"

def load(): return json.load(open(FILE)) if os.path.exists(FILE) else {}
def save(c): json.dump(c, open(FILE, "w"), indent=4)

def add():
    n, p, e = input("Name: "), input("Phone: "), input("Email: ")
    c = load()
    if n in c: return print("Exists.")
    c[n] = {"phone": p, "email": e}
    save(c); print("Added.")

def search():
    c = load(); n = input("Search: ")
    print(c[n] if n in c else "Not found.")

def update():
    c = load(); n = input("Update: ")
    if n not in c: return print("Not found.")
    c[n] = {"phone": input(f"Phone ({c[n]['phone']}): ") or c[n]['phone'],
            "email": input(f"Email ({c[n]['email']}): ") or c[n]['email']}
    save(c); print("Updated.")

def main():
    while (c := input("1-Add 2-Search 3-Update 4-Exit: ")) != "4":
        {"1": add, "2": search, "3": update}.get(c, lambda: print("Invalid"))()

if __name__ == "__main__": main()
