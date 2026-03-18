def greet_user(name: str) -> str:
    return f"Hallo, {name}! Willkommen bei Software Engineering."

if __name__ == "__main__":
    user_name = input("Geben Sie Ihren Namen ein: ")
    print(greet_user(user_name))
