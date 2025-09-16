from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import shop_controller
from lab4.app.my_project.auth.domain import Shop

shop_bp = Blueprint('shops', __name__, url_prefix='/shops')


@shop_bp.get('')
def get_all_shops() -> Response:
    """
    Get all shops
    ---
    tags:
        - Shops
    responses:
        200:
            description: A list of shops
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
                        client_id:
                            type: integer
                            example: 1
                        shop_adress_id:
                            type: integer
                            example: 1
    """
    return make_response(jsonify(shop_controller.find_all()), HTTPStatus.OK)


@shop_bp.post('')
def create_shop() -> Response:
    """
    Create a new shop
    ---
    tags:
        - Shops
    parameters:
      - name: Shop
        in: body
        required: true
        description: Shop object that needs to be added
        schema:
            type: object
            properties:
                client_id:
                    type: integer
                    example: 1
                shop_adress_id:
                    type: integer
                    example: 1
    responses:
        201:
            description: Shop created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    client_id:
                        type: integer
                        example: 1
                    shop_adress_id:
                        type: integer
                        example: 1
        500:
            description: Internal server error
    """
    content = request.get_json()
    shop = Shop.create_from_dto(content)
    shop_controller.create(shop)
    return make_response(jsonify(shop.put_into_dto()), HTTPStatus.CREATED)


@shop_bp.get('/<int:shop_id>')
def get_shop(shop_id: int) -> Response:
    """
    Get a shop by ID
    ---
    tags:
        - Shops
    parameters:
      - name: shop_id
        in: path
        required: true
        description: ID of the shop to retrieve
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Shop found
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    client_id:
                        type: integer
                        example: 1
                    shop_adress_id:
                        type: integer
                        example: 1
        404:
            description: Shop not found
    """
    return make_response(jsonify(shop_controller.find_by_id(shop_id)), HTTPStatus.OK)


@shop_bp.put('/<int:shop_id>')
def update_shop(shop_id: int) -> Response:
    """
    Update a shop by ID
    ---
    tags:
        - Shops
    parameters:
      - name: shop_id
        in: path
        required: true
        description: ID of the shop to update
        schema:
            type: integer
            example: 1
      - name: Shop
        in: body
        required: true
        description: Shop object that needs to be updated
        schema:
            type: object
            properties:
                client_id:
                    type: integer
                    example: 1
                shop_adress_id:
                    type: integer
                    example: 1
    responses:
        200:
            description: Shop updated
        404:
            description: Shop not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    shop = Shop.create_from_dto(content)
    shop_controller.update(shop_id, shop)
    return make_response("Shop updated", HTTPStatus.OK)


@shop_bp.patch('/<int:shop_id>')
def patch_shop(shop_id: int) -> Response:
    """
    Partially update a shop by ID
    ---
    tags:
        - Shops
    parameters:
      - name: shop_id
        in: path
        required: true
        description: ID of the shop to update
        schema:
            type: integer
            example: 1
      - name: Shop
        in: body
        required: true
        description: Shop object that needs to be updated (only include fields to be updated)
        schema:
            type: object
            properties:
                client_id:
                    type: integer
                    example: 1
                shop_adress_id:
                    type: integer
                    example: 1
    responses:
        200:
            description: Shop updated
        404:
            description: Shop not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    shop_controller.patch(shop_id, content)
    return make_response("Shop updated", HTTPStatus.OK)


@shop_bp.delete('/<int:shop_id>')
def delete_shop(shop_id: int) -> Response:
    """
    Delete a shop by ID
    ---
    tags:
        - Shops
    parameters:
      - name: shop_id
        in: path
        required: true
        description: ID of the shop to delete
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Shop deleted
        404:
            description: Shop not found
        500:
            description: Internal server error
    """
    shop_controller.delete(shop_id)
    return make_response("Shop deleted", HTTPStatus.OK)


@shop_bp.get('/get-shops-after-client/<int:client_id>')
def get_shops_after_client(client_id: int) -> Response:
    """
    Get shops by client ID
    ---
    tags:
        - Shops
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of shops for the given client ID
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        client_id:
                            type: integer
                            example: 1
                        name:
                            type: string
                            example: СІМ23
                        shop_id:
                            type: integer   
                            example: 1
    """
    return make_response(jsonify(shop_controller.get_shops_after_client(client_id)), HTTPStatus.OK)
