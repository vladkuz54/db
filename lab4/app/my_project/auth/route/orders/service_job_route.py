from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import service_job_controller
from lab4.app.my_project.auth.domain import ServiceJob

service_job_bp = Blueprint('service_jobs', __name__, url_prefix='/service-jobs')


@service_job_bp.get('')
def get_all_service_jobs() -> Response:
    """
    Get all service jobs
    ---
    tags:
        - Service Jobs
    responses:
        200:
            description: A list of service jobs
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
                        terminal_id:
                            type: integer
                            example: 1
                        service_type_id:
                            type: integer
                            example: 1
                        time_start:
                            type: string
                            format: date-time
                            example: "2025-01-01 10:00:00"
                        time_end:
                            type: string
                            format: date-time
                            example: "2025-01-01 12:00:00"
                        date:
                            type: string
                            format: date
                            example: "2025-01-01"
    """
    return make_response(jsonify(service_job_controller.find_all()), HTTPStatus.OK)


@service_job_bp.post('')
def create_service_job() -> Response:
    """
    Create a new service job
    ---
    tags:
        - Service Jobs
    parameters:
      - name: ServiceJob
        in: body
        required: true
        description: ServiceJob object that needs to be added
        schema:
            type: object
            properties:
                terminal_id:
                    type: integer
                    example: 1
                service_type_id:
                    type: integer
                    example: 1
                time_start:
                    type: string
                    format: date-time
                    example: "2025-01-01 10:00:00"
                time_end:
                    type: string
                    format: date-time
                    example: "2025-01-01 12:00:00"
                date:
                    type: string
                    format: date
                    example: "2025-01-01"
    responses:
        201:
            description: Service job created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    terminal_id:
                        type: integer
                        example: 1
                    service_type_id:
                        type: integer
                        example: 1
                    time_start:
                        type: string
                        format: date-time
                        example: "2025-01-01 10:00:00"
                    time_end:
                        type: string
                        format: date-time
                        example: "2025-01-01 12:00:00"
                    date:
                        type: string
                        format: date
                        example: "2025-01-01"
        400:
            description: Invalid input
        500:
            description: Internal server error  
    """
    content = request.get_json()
    service_job = ServiceJob.create_from_dto(content)
    service_job_controller.create(service_job)
    return make_response(jsonify(service_job.put_into_dto()), HTTPStatus.CREATED)


@service_job_bp.get('/<int:service_job_id>')
def get_service_job(service_job_id: int) -> Response:
    """
    Get service job by ID
    ---
    tags:
        - Service Jobs
    parameters:
      - name: service_job_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Service job found
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    terminal_id:
                        type: integer
                        example: 1
                    service_type_id:
                        type: integer
                        example: 1
                    time_start:
                        type: string
                        format: date-time
                        example: "2025-01-01 10:00:00"
                    time_end:
                        type: string
                        format: date-time
                        example: "2025-01-01 12:00:00"
                    date:
                        type: string
                        format: date
                        example: "2025-01-01"
        404:
            description: Service job not found
    """
    return make_response(jsonify(service_job_controller.find_by_id(service_job_id)), HTTPStatus.OK)


@service_job_bp.put('/<int:service_job_id>')
def update_service_job(service_job_id: int) -> Response:
    """
    Update a service job by ID
    ---
    tags:
        - Service Jobs
    parameters:
      - name: 
        in: path
        name: service_job_id
        required: true
        schema:
            type: integer
            example: 1
      - name: serviceJob
        in: body
        required: true
        description: ServiceJob object that needs to be updated
        schema:
            type: object
            properties:
                terminal_id:
                    type: integer
                    example: 1
                service_type_id:
                    type: integer
                    example: 1
                time_start:
                    type: string
                    format: date-time
                    example: "2025-01-01 10:00:00"
                time_end:
                    type: string
                    format: date-time
                    example: "2025-01-01 12:00:00"
                date:
                    type: string
                    format: date
                    example: "2025-01-01"
    responses:
        200:
            description: Service job updated
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    terminal_id:
                        type: integer
                        example: 1
                    service_type_id:
                        type: integer
                        example: 1
                    time_start:
                        type: string
                        format: date-time
                        example: "2025-01-01 10:00:00"
                    time_end:
                        type: string
                        format: date-time
                        example: "2025-01-01 12:00:00"
                    date:
                        type: string
                        format: date
                        example: "2025-01-01"
        404:
            description: Service job not found
        500:
            description: Internal server error  
    """
    content = request.get_json()
    service_job = ServiceJob.create_from_dto(content)
    service_job_controller.update(service_job_id, service_job)
    return make_response("Service job updated", HTTPStatus.OK)


@service_job_bp.patch('/<int:service_job_id>')
def patch_service_job(service_job_id: int) -> Response:
    """
    Partially update a service job by ID
    ---
    tags:
        - Service Jobs
    parameters:
      - name: service_job_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: serviceJob
        in: body
        required: true
        description: Fields to update in the service job
        schema:
            type: object
            properties:
                terminal_id:
                    type: integer
                    example: 1
                service_type_id:
                    type: integer
                    example: 1
                time_start:
                    type: string
                    format: date-time
                    example: "2025-01-01 10:00:00"
                time_end:
                    type: string
                    format: date-time
                    example: "2025-01-01 12:00:00"
                date:
                    type: string
                    format: date
                    example: "2025-01-01"
    responses:
        200:
            description: Service job updated
        404:
            description: Service job not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    service_job_controller.patch(service_job_id, content)
    return make_response("Service job updated", HTTPStatus.OK)


@service_job_bp.delete('/<int:service_job_id>')
def delete_service_job(service_job_id: int) -> Response:
    """
    Delete a service job by ID
    ---
    tags:
        - Service Jobs
    parameters:
      - name: service_job_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Service job deleted
        404:
            description: Service job not found
        500:
            description: Internal server error
    """
    service_job_controller.delete(service_job_id)
    return make_response("Service job deleted", HTTPStatus.OK)


@service_job_bp.get('/get-service-jobs-after-service-type/<int:service_type_id>')
def get_service_jobs_after_service_type(service_type_id: int) -> Response:
    """
    Get service jobs by service type ID
    ---
    tags:
        - Service Jobs
    parameters:
      - name: service_type_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of service jobs
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        name:
                            type: string
                            example: Звичайне обсуговування
                        service_job_id:
                            type: integer
                            example: 1
                        service_type_id:
                            type: integer
                            example: 1
    """
    return make_response(jsonify(service_job_controller.get_service_jobs_after_service_type(service_type_id)),
                         HTTPStatus.OK)

@service_job_bp.get('/get-service-jobs-after-terminal/<int:terminal_id>')
def get_service_jobs_after_terminal(terminal_id: int) -> Response:
    """
    Get service jobs by terminal ID
    ---
    tags:
        - Service Jobs
    parameters:
      - name: terminal_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of service jobs
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        manufacturer:
                            type: string
                            example: Samsung
                        service_job_id:
                            type: integer
                            example: 1
                        terminal_id:
                            type: integer
                            example: 1
    """
    return make_response(jsonify(service_job_controller.get_service_jobs_after_terminal(terminal_id)),
                         HTTPStatus.OK)
