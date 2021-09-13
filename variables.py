color = "Magenta"
city = "Washington, D.C."

def print_Cyan_Boston():
    color = "Cyan"
    city = "Boston"

    print_silver()

    print(color)
    print(city)

def print_silver():
    color = "Silver"
    print(color)

if __name__ == "__main__":
    # Expected output is Silver, Cyan, Boston, magenta, Washington, D.C.

    print_Cyan_Boston()

    print(color)
    print(city)
