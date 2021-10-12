def fizz_buzz(limit):
    for i in range(limit):
        if i % 3 == 0:
            print('fizz')
        if i % 5 == 0:
            print('fizz')
        if i % 3 and i % 5:
            print(i)

def main():
    fizz_buzz(10)

# finished code
#
# #!/usr/bin/env python
#
# def fizz_buzz(count):
#     for i in range(1, count+1):
#         if i % 15 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# 
# def main():
#     fizz_buzz(20)
# 
# if __name__ == "__main__":
#     main()
