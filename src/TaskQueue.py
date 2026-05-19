from typing import Iterable,Iterator
from src.models import Task
from src.logger import logger



class TaskQueueIterator:
    def __init__(self, tasks:list[Task])->None:
        """метод инит для итератора"""
        self._tasks = tasks
        self._index=0

    def __iter__(self)->Iterator[Task]:
        """возвращаем итератор"""
        return self

    def __next__(self)->Task:
        """пробегаемся по очереди"""
        if self._index >= len(self._tasks):
            raise StopIteration
        result=self._tasks[self._index]
        self._index+=1
        return result


class TaskQueue:
    def __init__(self,tasks:list[Task]):
        """метод init класса TaskQueue"""
        self._tasks = tasks

    def push(self,task:Task)->None:
        """метод добавления для очереди"""
        self._tasks.append(task)
        logger.info("добавлена задача")

    def pop(self)->Task:
        """метод удаления для очереди"""
        logger.info("задача удалена")
        return self._tasks.pop(0)

    def __len__(self)->int:
        logger.info("Длина очереди:")
        """возвращает длину очереди"""
        return len(self._tasks)

    def __iter__(self)->Iterator[Task]:
        """метод iter для нашей очереди"""
        logger.info("начался обход очереди")
        return TaskQueueIterator(self._tasks)

    def filter_by_status(self)->Iterable[Task]:
        """фильтр, который проверяет статус на true, если так, то он возвращает задачу"""
        for task in self._tasks:
            if task.status:
                logger.info("проверка на статус пройдена успешно")
                yield task

    def filter_by_priority(self,minimum_priority:int)->Iterable[Task]:
        """фильтр, который проверяет приоритет, если он больше минимального, то возвращаем задачу"""
        for task in self._tasks:
            if task.priority >= minimum_priority:
                logger.info("проверка на приоритет успешно пройдена")
                yield task

    def filter_by_id(self,minimum_id : int)->Iterable[Task]:
        """фильтр, который проверяет id, если он больше минимального, то возвращаем задачу"""
        for task in self._tasks:
            if task.id >= minimum_id:
                logger.info("проверка на id пройдена")
                yield task

    def filter_by_readiness_to_perform(self)->Iterable[Task]:
        """фильтр, который проверяет готовность на true, если так, то он возвращает задачу"""
        for task in self._tasks:
            if task.readiness_to_perform:
                logger.info("проверка на готовность пройдена")
                yield task

    def get_task_by_index(self,index:int)->Task | None:
        """метод, который возвращает задачу по индексу"""
        try:
            logger.info("получена задача по индексу")
            return self._tasks[index]
        except IndexError:
            return None






