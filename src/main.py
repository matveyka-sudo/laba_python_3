from src.generator_1 import Source
from src.generator_2 import Source1
from src.TaskQueue import TaskQueue
from src.proc import check


def main() -> None:
    '''Главная функция, точка входа в программу'''
    sources=[
        Source(),
        Source1("12.txt")
    ]
    result=check(sources)
    queue=TaskQueue(result)
    for task in queue:
        print(task)

if __name__ == "__main__":
    main()
