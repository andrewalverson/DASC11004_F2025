#!/usr/bin/env python3

import say_hello

def main():
    name = input("Enter your name, please: ")
    say_hello.greeting(name)

    num1, num2 = 4, 5
    
    sum = say_hello.add_these(num1, num2)
    print(sum)

if __name__ == "__main__":
    main()
