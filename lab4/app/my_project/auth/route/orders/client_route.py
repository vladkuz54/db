from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import client_controller
from lab4.app.my_project.auth.domain import Client

client_bp = Blueprint('clients', __name__, url_prefix='/clients')

@client_bp.get('')
def get_all_clients() -> Response:
    """
    Get all clients
    --- 
    tags:
      - Clients
    responses:
        200:
            description: A list of clients
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
                            example: Близенько
    """
    return make_response(jsonify(client_controller.find_all()), HTTPStatus.OK)


@client_bp.post('')
def create_client() -> Response:
    """
    Create a new client
    ---
    tags:
      - Clients
    parameters:
      - name: client
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Близенько
    responses:
        201:
            description: Client created
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
                        example: Близенько
        500:
            description: Internal server error
    """
    content = request.get_json()
    client = Client.create_from_dto(content)
    client_controller.create(client)
    return make_response(jsonify(client.put_into_dto()), HTTPStatus.CREATED)


@client_bp.get('/<int:client_id>')
def get_client(client_id: int) -> Response:
    """
    Get a client by ID
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A client object
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
                        example: Близенько
        404:
            description: Client not found
    """
    return make_response(jsonify(client_controller.find_by_id(client_id)), HTTPStatus.OK)


@client_bp.put('/<int:client_id>')
def update_client(client_id: int) -> Response:
    """
    Update a client by ID
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: client
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Близенько
    responses:
        200:
            description: Client updated
        404:
            description: Client not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    client = Client.create_from_dto(content)
    client_controller.update(client_id, client)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.patch('/<int:client_id>')
def patch_client(client_id: int) -> Response:
    """
    Partially update a client by ID
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: client
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Близенько
    responses:
        200:
            description: Client updated
        404:
            description: Client not found
        500:
            description: Internal server error   
    """
    content = request.get_json()
    client_controller.patch(client_id, content)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.delete('/<int:client_id>')
def delete_client(client_id: int) -> Response:
    """
    Delete a client by ID
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Client deleted
        404:
            description: Client not found
        500:
            description: Internal server error
    """
    client_controller.delete(client_id)
    return make_response("Client deleted", HTTPStatus.OK)


