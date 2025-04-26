import os
import random as r


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    main Every time it runs it outputs a random number between 1 and 6, simulating a dice rolling.

    Returns:
        Nothing
    """
    r.seed()
    dice_side = r.randint(1, 6)
    print(f"You rolled a {dice_side}!", end="\n\n")


if __name__ == "__main__":
    # cls()
    main()
