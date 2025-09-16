from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import terminal_controller
from lab4.app.my_project.auth.domain import Terminal

terminal_bp = Blueprint('terminals', __name__, url_prefix='/terminals')


@terminal_bp.get('')
def get_all_terminals() -> Response:
    """
    Get all terminals
    ---
    tags:
        - Terminals
    responses:
        200:
            description: A list of terminals
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                            example: 1
                        shop_id:
                            type: integer
                            example: 1
                        manufactures_id:
                            type: integer
                            example: 1
                        date_explotation:
                            type: string
                            format: date
                            example: "2025-01-01"
    """
    return make_response(jsonify(terminal_controller.find_all()), HTTPStatus.OK)


@terminal_bp.post('')
def create_terminal() -> Response:
    """
    Create a new terminal
    ---
    tags:
        - Terminals
    parameters:
      - name: Terminal
        in: body
        required: true
        description: Terminal object that needs to be added
        schema:
            type: object
            properties:
                shop_id:
                    type: integer
                    example: 1
                manufactures_id:
                    type: integer
                    example: 1
                date_explotation:
                    type: string
                    format: date
                    example: "2025-01-01"
    responses:
        201:
            description: Terminal created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    shop_id:
                        type: integer
                        example: 1
                    manufactures_id:
                        type: integer
                        example: 1
                    date_explotation:
                        type: string
                        format: date
                        example: "2025-01-01"
        500:
            description: Internal server error
    """
    content = request.get_json()
    terminal = Terminal.create_from_dto(content)
    terminal_controller.create(terminal)
    return make_response(jsonify(terminal.put_into_dto()), HTTPStatus.CREATED)


@terminal_bp.get('/<int:terminal_id>')
def get_terminal(terminal_id: int) -> Response:
    """
    Get terminal by ID
    ---
    tags:
        - Terminals
    parameters:
      - name: terminal_id
        in: path
        required: true
        description: ID of the terminal to retrieve
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Terminal found
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    shop_id:
                        type: integer
                        example: 1
                    manufactures_id:
                        type: integer
                        example: 1
                    date_explotation:
                        type: string
                        format: date
                        example: "2025-01-01"
        404:
            description: Terminal not found
        500:
            description: Internal server error
    """
    return make_response(jsonify(terminal_controller.find_by_id(terminal_id)), HTTPStatus.OK)


@terminal_bp.put('/<int:terminal_id>')
def update_terminal(terminal_id: int) -> Response:
    """
    Update a terminal by ID
    ---
    tags:
        - Terminals
    parameters:
      - name: terminal_id
        in: path
        required: true
        description: ID of the terminal to update
        schema:
            type: integer
            example: 1
      - name: Terminal
        in: body
        required: true
        description: Terminal object that needs to be updated
        schema:
            type: object
            properties:
                shop_id:
                    type: integer
                    example: 1
                manufactures_id:
                    type: integer
                    example: 1
                date_explotation:
                    type: string
                    format: date
                    example: "2025-01-01"
    responses:
        200:
            description: Terminal updated
        404:
            description: Terminal not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    terminal = Terminal.create_from_dto(content)
    terminal_controller.update(terminal_id, terminal)
    return make_response("Terminal updated", HTTPStatus.OK)


@terminal_bp.patch('/<int:terminal_id>')
def patch_terminal(terminal_id: int) -> Response:
    """
    Partially update a terminal by ID
    ---
    tags:
        - Terminals
    parameters:
      - name: terminal_id
        in: path
        required: true
        description: ID of the terminal to update
        schema:
            type: integer
            example: 1
      - name: Terminal
        in: body
        required: true
        description: Terminal object that needs to be updated
        schema:
            type: object
            properties:
                shop_id:
                    type: integer
                    example: 1
                manufactures_id:
                    type: integer
                    example: 1
                date_explotation:
                    type: string
                    format: date
                    example: "2025-01-01"
    responses:
        200:
            description: Terminal updated
        404:
            description: Terminal not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    terminal_controller.patch(terminal_id, content)
    return make_response("Terminal updated", HTTPStatus.OK)


@terminal_bp.delete('/<int:terminal_id>')
def delete_terminal(terminal_id: int) -> Response:
    """
    Delete a terminal by ID
    ---
    tags:
        - Terminals
    parameters:
      - name: terminal_id
        in: path
        required: true
        description: ID of the terminal to delete
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Terminal deleted
        404:
            description: Terminal not found
        500:
            description: Internal server error
    """
    terminal_controller.delete(terminal_id)
    return make_response("Terminal deleted", HTTPStatus.OK)


@terminal_bp.get('/get-terminals-after-shop/<int:shop_id>')
def get_terminals_after_shop(shop_id: int) -> Response:
    """
    Get terminals by shop ID
    ---
    tags:
        - Terminals
    parameters:
      - name: shop_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of terminals for the given shop ID
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        gps_latitude:
                            type: number
                            format: float
                            example: 50.4501
                        gps_longitude:
                            type: number
                            format: float
                            example: 30.5234
                        shop_id:
                            type: integer
                            example: 1
                        street:
                            type: string    
                            example: вулиця Тараса Шевченка
                        street_number:
                            type: string
                            example: 1
                        terminal_id:
                            type: integer
                            example: 1
    """
    return make_response(jsonify(terminal_controller.get_terminals_after_shop(shop_id)),
                         HTTPStatus.OK)


@terminal_bp.get('/get-terminals-after-manufacturer/<int:manufactures_id>')
def get_terminals_after_manufacturer(manufactures_id: int) -> Response:
    """
    Get terminals by manufacturer ID
    ---
    tags:
        - Terminals
    parameters:
      - name: manufactures_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of terminals for the given manufacturer ID
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        manufactures_id:
                            type: integer
                            example: 1
                        terminal_id:
                            type: integer
                            example: 1
                        name:
                            type: string
                            example: "Samsung"

    """
    return make_response(jsonify(terminal_controller.get_terminals_after_manufacturer(manufactures_id)),
                         HTTPStatus.OK)

