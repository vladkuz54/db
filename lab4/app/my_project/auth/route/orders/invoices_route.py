from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import invoices_controller
from lab4.app.my_project.auth.domain import Invoices

invoices_bp = Blueprint('invoices', __name__, url_prefix='/invoices')


@invoices_bp.get('')
def get_all_clients() -> Response:
    """
    Get all invoices
    ---
    tags:
        - Invoices
    responses:
        200:
            description: A list of invoices
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
                        service_job_id:
                            type: integer
                            example: 1
                        date:
                            type: string
                            format: date
                            example: "2025-01-01"
                        total_price:
                            type: number
                            format: float
                            example: 199.99
    """
    return make_response(jsonify(invoices_controller.find_all()), HTTPStatus.OK)


@invoices_bp.post('')
def create_client() -> Response:
    """
    Create a new invoice
    ---
    tags:
        - Invoices
    parameters:
      - name: invoice
        in: body
        required: true
        description: Invoice object that needs to be added
        schema:
            type: object
            properties:
                service_job_id:
                    type: integer
                    example: 1
                date:
                    type: string
                    format: date
                    example: "2025-01-01"
                total_price:
                    type: number
                    format: float
                    example: 199.99
    responses:
        201:
            description: Invoice created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    service_job_id:
                        type: integer
                        example: 1
                    date:
                        type: string
                        format: date
                        example: "2025-01-01"
                    total_price:
                        type: number
                        format: float
                        example: 199.99
        500:
            description: Internal server error
        """
    content = request.get_json()
    invoices = Invoices.create_from_dto(content)
    invoices_controller.create(invoices)
    return make_response(jsonify(invoices.put_into_dto()), HTTPStatus.CREATED)


@invoices_bp.get('/<int:invoices_id>')
def get_client(invoices_id: int) -> Response:
    """
    Get invoice by ID
    ---
    tags:
        - Invoices
    parameters:
      - name: invoices_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Invoice found
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    service_job_id:
                        type: integer
                        example: 1
                    date:
                        type: string
                        format: date
                        example: "2025-01-01"
                    total_price:
                        type: number
                        format: float
                        example: 199.99
        404:
            description: Invoice not found
    """
    return make_response(jsonify(invoices_controller.find_by_id(invoices_id)), HTTPStatus.OK)


@invoices_bp.put('/<int:invoices_id>')
def update_client(invoices_id: int) -> Response:
    """
    Update an invoice by ID
    ---
    tags:
        - Invoices
    parameters:
      - name: invoices_id
        in: path
        name: invoices_id
        required: true
        schema:
            type: integer
            example: 1
      - name: invoice
        in: body
        required: true
        schema:
            type: object
            properties:
                service_job_id:
                    type: integer
                    example: 1
                date:
                    type: string
                    format: date
                    example: "2025-01-01"
                total_price:
                    type: number
                    format: float
                    example: 199.99
    responses:
        200:
            description: Invoice updated
        404:
            description: Invoice not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    invoices = Invoices.create_from_dto(content)
    invoices_controller.update(invoices_id, invoices)
    return make_response("Invoice updated", HTTPStatus.OK)


@invoices_bp.patch('/<int:invoices_id>')
def patch_client(invoices_id: int) -> Response:
    """
    Partially update an invoice by ID
    ---
    tags:
        - Invoices
    parameters:
      - name: invoices_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: invoice
        in: body
        required: true
        schema:
            type: object
            properties:
                service_job_id:
                    type: integer
                    example: 1
                date:
                    type: string
                    format: date
                    example: "2025-01-01"
                total_price:
                    type: number
                    format: float
                    example: 199.99
    responses:
        200:
            description: Invoice updated
        404:
            description: Invoice not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    invoices_controller.patch(invoices_id, content)
    return make_response("Invoice updated", HTTPStatus.OK)


@invoices_bp.delete('/<int:invoices_id>')
def delete_client(invoices_id: int) -> Response:
    """
    Delete an invoice by ID
    ---
    tags:
        - Invoices
    parameters:
      - name: invoices_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Invoice deleted
        404:
            description: Invoice not found
        500:
            description: Internal server error
    """
    invoices_controller.delete(invoices_id)
    return make_response("Invoice deleted", HTTPStatus.OK)


