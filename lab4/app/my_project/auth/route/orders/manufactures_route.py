from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import manufactures_controller
from lab4.app.my_project.auth.domain import Manufactures

manufactures_bp = Blueprint('manufactures', __name__, url_prefix='/manufactures')


@manufactures_bp.get('')
def get_all_manufactures() -> Response:
    """
    Get all manufactures
    ---
    tags:
        - Manufactures
    responses:
        200:
            description: A list of manufactures
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
                        name:
                            type: string
                            example: Samsung
    """
    return make_response(jsonify(manufactures_controller.find_all()), HTTPStatus.OK)


@manufactures_bp.post('')
def create_manufacture() -> Response:
    """
    Create a new manufacture
    ---
    tags:
        - Manufactures
    parameters:
      - name: manufacture
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Samsung
    responses:
        201:
            description: Manufacture created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    name:
                        type: string
                        example: Samsung
        500:
            description: Internal server error
    """
    content = request.get_json()
    manufactures = Manufactures.create_from_dto(content)
    manufactures_controller.create(manufactures)
    return make_response(jsonify(manufactures.put_into_dto()), HTTPStatus.CREATED)


@manufactures_bp.get('/<int:manufacture_id>')
def get_manufacture(manufacture_id: int) -> Response:
    """
    Get a manufacture by ID
    ---
    tags:
        - Manufactures
    parameters:
      - name: manufacture_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Manufacture found
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    name:
                        type: string
                        example: Samsung
        404:
            description: Manufacture not found
    """
    return make_response(jsonify(manufactures_controller.find_by_id(manufacture_id)), HTTPStatus.OK)


@manufactures_bp.put('/<int:manufacture_id>')
def update_manufacture(manufacture_id: int) -> Response:
    """
    Update a manufacture by ID
    ---
    tags:
        - Manufactures
    parameters:
      - name: manufacture_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: manufacture
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Samsung
    responses:
        200:
            description: Manufacture updated
        404:
            description: Manufacture not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    manufactures = Manufactures.create_from_dto(content)
    manufactures_controller.update(manufacture_id, manufactures)
    return make_response("Manufacture updated", HTTPStatus.OK)


@manufactures_bp.patch('/<int:manufacture_id>')
def patch_manufacture(manufacture_id: int) -> Response:
    """
    Partially update a manufacture by ID
    ---
    tags:
        - Manufactures
    parameters:
      - name: manufacture_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: manufacture
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Samsung
    responses:
        200:
            description: Manufacture updated
        404:
            description: Manufacture not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    manufactures_controller.patch(manufacture_id, content)
    return make_response("Manufacture updated", HTTPStatus.OK)


@manufactures_bp.delete('/<int:manufacture_id>')
def delete_manufacture(manufacture_id: int) -> Response:
    """
    Delete a manufacture by ID
    ---
    tags:
        - Manufactures
    parameters:
      - name: manufacture_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Manufacture deleted
        404:
            description: Manufacture not found
        500:
            description: Internal server error
    """
    manufactures_controller.delete(manufacture_id)
    return make_response("Manufacture deleted", HTTPStatus.OK)