import sys

def sum_two_numbers(a: float, b: float) -> float:
              """Return the sum of two numbers (accepts int or float)."""
              return a + b


if __name__ == "__main__":

              def parse_arg(x: str) -> float:
                            try:
                                          return float(x)
                            except ValueError:
                                          raise SystemExit("Please provide numeric values.")

              if len(sys.argv) >= 3:
                            a = parse_arg(sys.argv[1])
                            b = parse_arg(sys.argv[2])
              else:
                            try:
                                          a = parse_arg(input("Enter first number: "))
                                          b = parse_arg(input("Enter second number: "))
                            except (EOFError, KeyboardInterrupt):
                                          raise SystemExit()

              result = sum_two_numbers(a, b)
              # print as int when both inputs are whole numbers
              if float(a).is_integer() and float(b).is_integer():
                            print(int(result))
              else:
                            print(result)