from src.generator_1 import Source
from src.generator_2 import Source1
from src.proc import check


def main() -> None:
    '''Главная функция, точка входа в программу'''
    sources=[
        Source(),
        Source1("12.txt")
    ]
    result=check(sources)
    for task in result:
        print(task)

if __name__ == "__main__":
    main()
