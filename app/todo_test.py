from .todo import TodoParams, TodoService
from faker import Faker

faker = Faker()

sut = TodoService()

def make_params() -> TodoParams:
    return TodoParams(
        description=faker.word(),
        owner=faker.name()
    )

def test_should_return_correct_response_on_success_add_todo():
    params = make_params()
    result = sut.add_todo(params)
    assert result.description == params.description
    assert result.owner == params.owner

def test_should_return_correct_response_on_success_get_todos():
    sut.reset_todos()
    params = make_params()
    sut.add_todo(params)
    result = sut.get_todos()
    assert result.todos[0].description == params.description
    assert result.todos[0].owner == params.owner
