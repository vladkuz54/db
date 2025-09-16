from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import masters_controller
from lab4.app.my_project.auth.domain import Masters

masters_bp = Blueprint('masters', __name__, url_prefix='/masters')


@masters_bp.get('')
def get_all_masters() -> Response:
    """
    Get all masters
    ---
    tags:
        - Masters
    responses:
        200:
            description: A list of masters
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
                        surname:
                            type: string
                            example: Іванченко
                        first_name:
                            type: string
                            example: Іван
                        patronymic:
                            type: string
                            example: Іванович
                        phone_number:
                            type: string
                            example: 2319993456
    """
    return make_response(jsonify(masters_controller.find_all()), HTTPStatus.OK)


@masters_bp.post('')
def create_master() -> Response:
    """
    Create a new master
    ---
    tags:
        - Masters
    parameters:
      - name: master
        in: body
        required: true
        description: Master object that needs to be added
        schema:
            type: object
            properties:
                surname:
                    type: string
                    example: Іванченко
                first_name:
                    type: string
                    example: Іван
                patronymic:
                    type: string
                    example: Іванович
                phone_number:
                    type: string
                    example: 2319993456
    responses:
        201:
            description: Master created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    surname:
                        type: string
                        example: Іванченко
                    first_name:
                        type: string
                        example: Іван
                    patronymic:
                        type: string
                        example: Іванович
                    phone_number:
                        type: string
                        example: 2319993456
        500:
            description: Internal server error
    """
    content = request.get_json()
    masters = Masters.create_from_dto(content)
    masters_controller.create(masters)
    return make_response(jsonify(masters.put_into_dto()), HTTPStatus.CREATED)


@masters_bp.get('/<int:master_id>')
def get_master(master_id: int) -> Response:
    """
    Get a master by ID
    ---
    tags:
        - Masters
    parameters:
      - name: master_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Master found
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    surname:
                        type: string
                        example: Іванченко
                    first_name:
                        type: string
                        example: Іван
                    patronymic:
                        type: string
                        example: Іванович
                    phone_number:
                        type: string
                        example: 2319993456
        404:
            description: Master not found
    """
    return make_response(jsonify(masters_controller.find_by_id(master_id)), HTTPStatus.OK)


@masters_bp.put('/<int:master_id>')
def update_master(master_id: int) -> Response:
    """
    Update a master by ID
    ---
    tags:
        - Masters
    parameters:
      - name: master_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: master
        in: body
        required: true
        description: Master object that needs to be updated
        schema:
            type: object
            properties:
                surname:
                    type: string
                    example: Іванченко
                first_name:
                    type: string
                    example: Іван
                patronymic:
                    type: string
                    example: Іванович
                phone_number:
                    type: string
                    example: 2319993456
    responses:
        200:
            description: Master updated
        404:
            description: Master not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    masters = Masters.create_from_dto(content)
    masters_controller.update(master_id, masters)
    return make_response("Master updated", HTTPStatus.OK)


@masters_bp.patch('/<int:master_id>')
def patch_master(master_id: int) -> Response:
    """
    Partially update a master by ID
    ---
    tags:
        - Masters
    parameters:
      - name: master_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: master
        in: body
        required: true
        description: Fields to update in the master object
        schema:
            type: object
            properties:
                surname:
                    type: string
                    example: Іванченко
                first_name:
                    type: string
                    example: Іван
                patronymic:
                    type: string
                    example: "Smith"
                phone_number:
                    type: string
                    example: 2319993456
    responses:
        200:
            description: Master updated
        404:
            description: Master not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    masters_controller.patch(master_id, content)
    return make_response("Master updated", HTTPStatus.OK)


@masters_bp.delete('/<int:master_id>')
def delete_master(master_id: int) -> Response:
    """
    Delete a master by ID
    ---
    tags:
        - Masters
    parameters:
      - name: master_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Master deleted
        404:
            description: Master not found
        500:
            description: Internal server error
    """
    masters_controller.delete(master_id)
    return make_response("Master deleted", HTTPStatus.OK)