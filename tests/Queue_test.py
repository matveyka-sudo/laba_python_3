import pytest
from datetime import datetime
from src.models import Task
from src.TaskQueue import TaskQueue

@pytest.fixture
def valid_tasks():
    """Создает набор задач для тестирования очереди"""
    return [
        Task(id=1, description="low", priority=1,
             status=False, time=datetime.now(), readiness_to_perform=False),
        Task(id=2, description="high", priority=10,
             status=True, time=datetime.now(), readiness_to_perform=False),
        Task(id=3, description="medium", priority=5,
             status=False, time=datetime.now(), readiness_to_perform=True),
    ]

@pytest.fixture
def queue(valid_tasks):
    """Инициализирует очередь перед каждым тестом"""
    return TaskQueue(valid_tasks)

def test_filter_by_status(queue):
    """тест фильтра по статусу"""
    result=list(queue.filter_by_status())
    assert result[0].id == 2
    assert result[0].description == "high"

def test_filter_by_priority(queue):
    '''тест фильтра по приоритету'''
    result=list(queue.filter_by_priority(9))
    assert result[0].id == 2
    assert result[0].description == "high"

def test_filter_by_id(queue):
    """тест фильтра по id"""
    result=list(queue.filter_by_id(3))
    assert result[0].id == 3
    assert result[0].description == "medium"

def test_filter_by_readiness(queue):
    """тест фильтра по готовности"""
    result=list(queue.filter_by_readiness_to_perform())
    assert result[0].id == 3
    assert result[0].description == "medium"

def test_by_pop(queue):
    """тестирования метода pop"""
    result=queue.pop()
    assert result.id == 3

def test_by_len(queue):
    """тестирование магического метода __len__"""
    result=queue.__len__()
    assert result == 3

def test_by_push(queue):
    """тестирование метода push"""
    queue.push(Task(id = 4, description = "description", priority = 15, status = True, time = datetime.now(), readiness_to_perform = True))
    result=queue.pop()
    assert result.id == 4

def test_get_task_by_index(queue):
    """тестирование метода получения задачи по индексу"""
    result=queue.get_task_by_index(2)
    assert result.id == 3

def test_get_next_task(queue):
    """тест получения метода получения следующей задачи"""
    result=queue.get_next_task()
    assert result.id == 1





