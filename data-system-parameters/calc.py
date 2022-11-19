# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys


def main():
    """Implement the calculator"""
    if len(sys.argv) < 4 or sys.argv[2] not in '+-*/':
        return 'Error'
    #breakpoint()
    match sys.argv[2] :
        case '+':
            return int(sys.argv[1]) + int(sys.argv[3])
        case '-':
            return int(sys.argv[1]) - int(sys.argv[3])
        case '*':
            return int(sys.argv[1]) * int(sys.argv[3])
        case '/':
            return int(sys.argv[1]) / int(sys.argv[3])

    return 'Oi'


if __name__ == "__main__":
    print(main())
