from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import service_job_masters_controller
from lab4.app.my_project.auth.domain import ServiceJobMasters

service_job_masters_bp = Blueprint('service_job_masters', __name__, url_prefix='/service-job-masters')


@service_job_masters_bp.get('')
def get_all_service_job_masters() -> Response:
    """
    Get all service job masters
    ---
    tags:
        - Service Job Masters
    responses:
        200:
            description: A list of service job masters
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
                        master_id:
                            type: integer
                            example: 1
    """
    return make_response(jsonify(service_job_masters_controller.find_all()), HTTPStatus.OK)


@service_job_masters_bp.post('')
def create_service_job_master() -> Response:
    """
    Create a new service job master
    ---
    tags:
        - Service Job Masters
    parameters:
      - name: service_job_master
        in: body
        required: true
        description: ServiceJobMaster object that needs to be added
        schema:
            type: object
            properties:
                service_job_id:
                    type: integer
                    example: 1
                master_id:
                    type: integer
                    example: 1
    responses:
        201:
            description: Service job master created
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
                    master_id:
                        type: integer
                        example: 1
        500:
            description: Internal server error
    """
    content = request.get_json()
    service_job_masters = ServiceJobMasters.create_from_dto(content)
    service_job_masters_controller.create(service_job_masters)
    return make_response(jsonify(service_job_masters.put_into_dto()), HTTPStatus.CREATED)


@service_job_masters_bp.get('/<int:service_job_masters_id>')
def get_service_job_master(service_job_masters_id: int) -> Response:
    """
    Get a service job master by ID
    ---
    tags:
        - Service Job Masters
    parameters:
      - name: service_job_masters_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Service job master found
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
                    master_id:
                        type: integer
                        example: 1
        404:
            description: Service job master not found
    """
    return make_response(jsonify(service_job_masters_controller.find_by_id(service_job_masters_id)), HTTPStatus.OK)


@service_job_masters_bp.put('/<int:service_job_masters_id>')
def update_service_job_master(service_job_masters_id: int) -> Response:
    """
    Update a service job master by ID
    ---
    tags:
        - Service Job Masters
    parameters:
      - name: service_job_masters_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: service_job_master
        in: body
        required: true
        description: ServiceJobMaster object that needs to be updated
        schema:
            type: object
            properties:
                service_job_id:
                    type: integer
                    example: 1
                master_id:
                    type: integer
                    example: 1
    responses:
        200:
            description: Service job master updated
        404:
            description: Service job master not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    service_job_masters = ServiceJobMasters.create_from_dto(content)
    service_job_masters_controller.update(service_job_masters_id, service_job_masters)
    return make_response("Service job masters updated", HTTPStatus.OK)


@service_job_masters_bp.patch('/<int:service_job_masters_id>')
def patch_service_job_master(service_job_masters_id: int) -> Response:
    """
    Partially update a service job master by ID
    ---
    tags:
        - Service Job Masters
    parameters:
      - name: service_job_masters_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: service_job_master
        in: body
        required: true
        description: Fields to be updated in the service job master
        schema:
            type: object
            properties:
                service_job_id:
                    type: integer
                    example: 1
                master_id:
                    type: integer
                    example: 1
    responses:
        200:
            description: Service job master updated
        404:
            description: Service job master not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    service_job_masters_controller.patch(service_job_masters_id, content)
    return make_response("Service job masters updated", HTTPStatus.OK)


@service_job_masters_bp.delete('/<int:service_job_masters_id>')
def delete_service_job_master(service_job_masters_id: int) -> Response:
    """
    Delete a service job master by ID
    ---
    tags:
        - Service Job Masters
    parameters:
      - name: service_job_masters_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Service job master deleted
        404:
            description: Service job master not found
        500:
            description: Internal server error
    """
    service_job_masters_controller.delete(service_job_masters_id)
    return make_response("Service job masters deleted", HTTPStatus.OK)


@service_job_masters_bp.get('/get-masters-after-service-job/<int:service_job_id>')
def get_masters_after_service_jobs(service_job_id: int) -> Response:
    """
    Get all masters associated with a specific service job ID
    ---
    tags:
        - Service Job Masters 
    parameters:
      - name: service_job_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of masters associated with the service job ID
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
                        master_id:
                            type: integer
                            example: 1
                        phone_number:
                            type: string
                            example: 759530853
                        service_job_id:
                            type: integer
                            example: 1
                        surname:
                            type: string
                            example: Іванченко
    """
    return make_response(jsonify(service_job_masters_controller.get_masters_after_service_jobs(service_job_id)),
                         HTTPStatus.OK)


@service_job_masters_bp.get('/get-service-jobs-after-master/<int:master_id>')
def get_service_job_after_masters(master_id: int) -> Response:
    """
    Get all service jobs associated with a specific master ID
    ---
    tags:
        - Service Job Masters
    parameters:
      - name: master_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of service jobs associated with the master ID
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        master_id:
                            type: integer
                            example: 1
                        service_job_id:
                            type: integer
                            example: 1
                        service_type_id:
                            type: integer
                            example: 1
    """
    return make_response(jsonify(service_job_masters_controller.get_service_job_after_masters(master_id)),
                         HTTPStatus.OK)
