
from typing import List
from time import time
from pydantic import BaseModel

class TodoParams(BaseModel):
    description: str
    owner: str

class AddTodoResponse(BaseModel):
    description: str
    owner: str
    timestamp: int

class GetTodosResponse(BaseModel):
    todos: List[AddTodoResponse]

class TodoService():

    def __init__(self):
        self.todos = []

    def add_todo(self, todo: TodoParams) -> AddTodoResponse:
        todo = AddTodoResponse(
            description=todo.description,
            owner=todo.owner,
            timestamp=int(time())
        )
        self.todos.append(todo.__dict__)
        return todo

    def get_todos(self) -> GetTodosResponse:
        return GetTodosResponse(todos=self.todos)

    def reset_todos(self):
        self.todos = []
