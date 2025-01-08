
def main():
    
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    
    print("\nNumbers from 1 to n:")
    for i in range(1, n + 1):
        print(i)

    
    total = 0
    current = 1
    while current <= n:
        total += current
        current += 1

    
    print(f"\nThe sum of numbers from 1 to {n} is: {total}")

if __name__ == "__main__":
    main()
