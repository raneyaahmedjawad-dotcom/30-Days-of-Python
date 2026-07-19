visitors = set()

while True:
    name = input("Enter visitor name (or type 'done'): ")

    if name.lower() == "done":
        break

    visitors.add(name)

print("\n===== UNIQUE VISITORS =====")

for visitor in visitors:
    print(visitor)

print(f"\nTotal Unique Visitors: {len(visitors)}")