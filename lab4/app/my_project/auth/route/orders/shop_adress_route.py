from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import shop_adress_controller
from lab4.app.my_project.auth.domain import Shop_Adress

shop_adress_bp = Blueprint('shop_adresses', __name__, url_prefix='/shop-adresses')


@shop_adress_bp.get('')
def get_all_shop_adresses() -> Response:
    """
    Get all shop adresses
    ---
    tags:
        - Shop Adresses
    responses:
        200:
            description: A list of shop adresses
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
                        street:
                            type: string
                            example: вулиця Тараса Шевченка
                        street_number:
                            type: integer
                            example: 1
                        gps_latitude:
                            type: number
                            example: 40.7128
                        gps_longitude:
                                    type: number
                                    example: -74.0060
    """
    return make_response(jsonify(shop_adress_controller.find_all()), HTTPStatus.OK)


@shop_adress_bp.post('')
def create_shop_adress() -> Response:
    """
    Create a new shop adress
    ---
    tags:
        - Shop Adresses
    parameters:
      - name: Shop_Adress
        in: body
        required: true
        description: Shop_Adress object that needs to be added
        schema:
            type: object
            properties:
                street:
                    type: string
                    example: вулиця Тараса Шевченка
                street_number:
                    type: integer
                    example: 1
                gps_latitude:
                    type: number
                    example: 40.7128
                gps_longitude:
                    type: number
                    example: -74.0060
    responses:
        201:
            description: Shop adress created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    street:
                        type: string
                        example: вулиця Тараса Шевченка
                    street_number:
                        type: integer
                        example: 1
                    gps_latitude:
                        type: number
                        example: 40.7128
                    gps_longitude:
                        type: number
                        example: -74.0060
        500:
            description: Internal server error
    """
    content = request.get_json()
    shop_adress = Shop_Adress.create_from_dto(content)
    shop_adress_controller.create(shop_adress)
    return make_response(jsonify(shop_adress.put_into_dto()), HTTPStatus.CREATED)


@shop_adress_bp.get('/<int:shop_adress_id>')
def get_shop_adress(shop_adress_id: int) -> Response:
    """
    Get a shop adress by ID
    ---
    parameters:
      - name: shop_adress_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
        description: ID of the shop adress to retrieve
    tags:
        - Shop Adresses
    responses:
        200:
            description: Shop adress found
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    street:
                        type: string
                        example: вулиця Тараса Шевченка
                    street_number:
                        type: integer
                        example: 1
                    gps_latitude:
                        type: number
                        example: 40.7128
                    gps_longitude:
                        type: number
                        example: -74.0060
        404:
            description: Shop adress not found
    """
    return make_response(jsonify(shop_adress_controller.find_by_id(shop_adress_id)), HTTPStatus.OK)


@shop_adress_bp.put('/<int:shop_adress_id>')
def update_shop_adress(shop_adress_id: int) -> Response:
    """
    Update a shop adress by ID
    ---
    tags:
        - Shop Adresses 
    parameters:
      - name: shop_adress_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
        description: ID of the shop adress to update
      - name: Shop_Adress
        in: body
        required: true
        description: Shop_Adress object that needs to be updated
        schema:
            type: object
            properties:
                street:
                    type: string
                    example: вулиця Тараса Шевченка
                street_number:
                    type: integer
                    example: 1
                gps_latitude:
                    type: number
                    example: 40.7128
                gps_longitude:
                    type: number
                    example: -74.0060
    responses:
        200:
            description: Shop adress updated
        404:
            description: Shop adress not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    shop_adress = Shop_Adress.create_from_dto(content)
    shop_adress_controller.update(shop_adress_id, shop_adress)
    return make_response("Shop adress was updated", HTTPStatus.OK)


@shop_adress_bp.patch('/<int:shop_adress_id>')
def patch_shop_adress(shop_adress_id: int) -> Response:
    """
    Partially update a shop adress by ID
    ---
    tags:
        - Shop Adresses
    parameters:
      - name: shop_adress_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
        description: ID of the shop adress to update
      - name: Shop_Adress
        in: body
        required: true
        description: Shop_Adress object that needs to be updated
        schema:
            type: object
            properties:
                street:
                    type: string
                    example: вулиця Тараса Шевченка
                street_number:
                    type: integer
                    example: 1
                gps_latitude:
                    type: number
                    example: 40.7128
                gps_longitude:
                    type: number
                    example: -74.0060
    responses:
        200:
            description: Shop adress updated
        404:
            description: Shop adress not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    shop_adress_controller.patch(shop_adress_id, content)
    return make_response("Shop adress was updated", HTTPStatus.OK)


@shop_adress_bp.delete('/<int:shop_adress_id>')
def delete_shop_adress(shop_adress_id: int) -> Response:
    """
    Delete a shop adress by ID
    ---
    tags:
        - Shop Adresses
    parameters:
      - name: shop_adress_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
        description: ID of the shop adress to delete
    responses:
        200:
            description: Shop adress deleted
        404:
            description: Shop adress not found
        500:
            description: Internal server error
    """
    shop_adress_controller.delete(shop_adress_id)
    return make_response("Shop adress was deleted", HTTPStatus.OK)
