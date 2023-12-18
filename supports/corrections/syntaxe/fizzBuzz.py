def fizz_buzz_1():
    for i in range(100 + 1):
        to_print = ""
        if i % 3 == 0:
            to_print += "fizz"
        if i % 5 == 0:
            to_print += "buzz"

        if not to_print:
            to_print = str(i)

        print(to_print)


def fizz_buzz_2():
    def rule(n):
        return (
            "fizz" * (n % 3 == 0) + "buzz" * (n % 5 == 0) or str(n)
        )
    print("\n".join(map(rule, range(101))))
