from http import HTTPStatus
from todo import AddTodoResponse, GetTodosResponse, TodoService, TodoParams
from fastapi import FastAPI

app = FastAPI(
    title='Workshop Serverless CI/CD',
    version='1.0.0',
)

todo_service = TodoService()

@app.post(
    '/todo',
    responses={
        HTTPStatus.CREATED.value: {'model': AddTodoResponse, 'description': 'TODO created'},
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {'description': 'Internal Server Error'}
    },
    status_code=HTTPStatus.CREATED,
    tags=['Todo']
)
def add_todo(body: TodoParams):
    return todo_service.add_todo(body)


@app.get(
    '/todo',
    responses={
        HTTPStatus.OK.value: {'model': GetTodosResponse, 'description': 'Ok'},
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {'description': 'Internal Server Error'}
    },
    status_code=HTTPStatus.OK,
    tags=['Todo']
)
def get_todo():
    return todo_service.get_todos()
