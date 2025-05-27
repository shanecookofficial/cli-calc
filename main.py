from src.utils.handler import Handler

def main() -> None:

    handler = Handler()

    while True:

        # TODO: Add some kind of command handler. For now in the MVP the only command should be q
        user_input = input("> ")

        if user_input == "q":
            break

        print(handler.solve(user_input))

if __name__ == "__main__":
    main()