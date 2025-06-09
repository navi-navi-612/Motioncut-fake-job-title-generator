import random

adjectives = ["Certified", "Global", "Senior", "Dynamic", "Lead", "Quantum", "Funky"]
roles = ["Meme", "Unicorn", "Algorithm", "Banana", "AI", "Cloud", "Penguin"]
suffixes = ["Strategist", "Engineer", "Manager", "Consultant", "Ninja", "Overlord"]

while True:
    adj = random.choice(adjectives)
    role = random.choice(roles)
    suf = random.choice(suffixes)

    job_title = f"{adj} {role} {suf}"
    print(f"\n💼 Your fake job title is: {job_title}")

    again = input("Want another one? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! 🚀")
        break