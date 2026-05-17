from typing import Iterable
from src.models import Task
from src.logger import logger

class TaskQueue:
    def __init__(self,tasks:list[Task]):
        """метод init класса TaskQueue"""
        self._tasks = tasks
        self._iter = None

    def push(self,task:Task)->None:
        """метод добавления для очереди"""
        self._tasks.append(task)
        logger.info("добавлена задача")
        self._iter = None

    def pop(self)->Task:
        """метод удаления для очереди"""
        self._iter = None
        logger.info("задача удалена")
        return self._tasks.pop(0)

    def __len__(self)->int:
        logger.info("Длина очереди:")
        """возвращает длину очереди"""
        return len(self._tasks)

    def __iter__(self):
        """метод iter для нашей очереди"""
        return iter(self._tasks)

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

    def get_next_task(self)->Task | None:
        """метод, позволяющий получить следующую задачу"""
        if self._iter is None:
            self._iter = iter(self._tasks)
        try:
            logger.info("Следующая задача:")
            return next(self._iter)
        except StopIteration:
            self._iter = None
            return None

    def get_task_by_index(self,index:int)->Task | None:
        """метод, который возвращает задачу по индексу"""
        try:
            logger.info("получена задача по индексу")
            return self._tasks[index]
        except IndexError:
            return None






