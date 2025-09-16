from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import service_type_controller
from lab4.app.my_project.auth.domain import ServiceType

service_type_bp = Blueprint('service_types', __name__, url_prefix='/service-types')


@service_type_bp.get('')
def get_all_service_types() -> Response:
    """
    Get all service types
    ---
    tags:
        - Service Types
    responses:
        200:
            description: A list of service types
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
                            example: Звичайне обсуговування
    """
    return make_response(jsonify(service_type_controller.find_all()), HTTPStatus.OK)


@service_type_bp.post('')
def create_service_type() -> Response:
    """
    Create a new service type
    ---
    tags:
        - Service Types
    parameters:
      - name: ServiceType
        in: body
        required: true
        description: ServiceType object that needs to be added
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Звичайне обсуговування
    responses:
        201:
            description: Service type created
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
                        example: Звичайне обсуговування
        500:
            description: Internal server error
    """
    content = request.get_json()
    service_type = ServiceType.create_from_dto(content)
    service_type_controller.create(service_type)
    return make_response(jsonify(service_type.put_into_dto()), HTTPStatus.CREATED)


@service_type_bp.get('/<int:service_type_id>')
def get_service_type(service_type_id: int) -> Response:
    """
    Get a service type by ID
    ---
    tags:
        - Service Types
    parameters:
      - name: service_type_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
        description: ID of the service type to retrieve
    responses:
        200:
            description: Service type found
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
                        example: Звичайне обсуговування
        404:
            description: Service type not found
    """
    return make_response(jsonify(service_type_controller.find_by_id(service_type_id)), HTTPStatus.OK)


@service_type_bp.put('/<int:service_type_id>')
def update_service_type(service_type_id: int) -> Response:
    """
    Update a service type by ID
    ---
    tags:
        - Service Types
    parameters:
      - name: service_type_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
        description: ID of the service type to update
      - name: ServiceType
        in: body
        required: true
        description: ServiceType object that needs to be updated
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Звичайне обсуговування
    responses:
        200:
            description: Service type updated
        404:
            description: Service type not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    service_type = ServiceType.create_from_dto(content)
    service_type_controller.update(service_type_id, service_type)
    return make_response("Service type updated", HTTPStatus.OK)


@service_type_bp.patch('/<int:service_type_id>')
def patch_service_type(service_type_id: int) -> Response:
    """
    Partially update a service type by ID
    ---
    tags:
        - Service Types
    parameters: 
      - name: service_type_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
        description: ID of the service type to update
      - name: ServiceType
        in: body
        required: true
        description: Fields to update in the service type
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Звичайне обсуговування
    responses:
        200:
            description: Service type updated
        404:
            description: Service type not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    service_type_controller.patch(service_type_id, content)
    return make_response("Service type updated", HTTPStatus.OK)


@service_type_bp.delete('/<int:service_type_id>')
def delete_service_type(service_type_id: int) -> Response:
    """
    Delete a service type by ID
    ---
    tags:
        - Service Types
    parameters:
      - name: service_type_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
        description: ID of the service type to delete
    responses:
        200:
            description: Service type deleted
        404:
            description: Service type not found
        500:
            description: Internal server error
    """
    service_type_controller.delete(service_type_id)
    return make_response("Service type deleted", HTTPStatus.OK)