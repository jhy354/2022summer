if __name__ == "__main__":
    n = int(input("n:"))
    
    sum = 0
    for i in range(1, n+1):
        sum += i
    
    print(f"Sum = {sum}")

    exit(0)