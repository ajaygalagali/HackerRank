def print_formatted(number):
    # your code goes here
    for i in range(1, n + 1):
        width = len(str(bin(number)).replace("0b", ""))
        octal = oct(i)
        hexd = str(hex(i))
        binary = bin(i)
        print(str(i).rjust(width, " "), octal.replace("0o", "").rjust(width, " "),
              hexd.replace("0x", "").upper().rjust(width, " "), binary.replace("0b", "").rjust(width, " "))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

