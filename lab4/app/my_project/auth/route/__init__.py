import json
import os
from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.shop_route import shop_bp
    from .orders.client_route import client_bp
    from .orders.shop_adress_route import shop_adress_bp
    from .orders.manufactures_route import manufactures_bp
    from .orders.service_type_route import service_type_bp
    from .orders.masters_route import masters_bp
    from .orders.terminal_route import terminal_bp
    from .orders.service_job_route import service_job_bp
    from .orders.service_job_masters_route import service_job_masters_bp
    from .orders.invoices_route import invoices_bp

    app.register_blueprint(shop_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(shop_adress_bp)
    app.register_blueprint(manufactures_bp)
    app.register_blueprint(service_type_bp)
    app.register_blueprint(masters_bp)
    app.register_blueprint(terminal_bp)
    app.register_blueprint(service_job_bp)
    app.register_blueprint(service_job_masters_bp)
    app.register_blueprint(invoices_bp)

    @app.get('/')
    def home():
        return render_template('index.html')
    
    @app.get('/register')
    def register_form():
        return render_template('register.html')

    @app.get("/login")
    def login_form():
        return render_template("login.html")

    @app.post('/register')
    def register():
        from lab4.app.my_project.auth.domain import Account
        from lab4.app.my_project import db

        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        if not email or not password:
            return jsonify({"msg": "Enter email and password"}), 400

        if Account.query.filter((Account.email == email)).first():
            return jsonify({"msg": "User with this email already exists"}), 400

        hashed_password = generate_password_hash(password)
        new_acc = Account(email=email, password=hashed_password)
        db.session.add(new_acc)
        db.session.commit()
        return jsonify({"msg": "Registration successful!"}), 200

    @app.post("/login")
    def login():
        from lab4.app.my_project.auth.domain import Account

        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        user = Account.query.filter(Account.email == email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"msg": "Bad email or password"}), 401

        access_token = create_access_token(identity=user.email)
        return jsonify(access_token=access_token)

    @app.route('/logout')
    def logout():
        resp = make_response(redirect(url_for('home')))
        resp.set_cookie('access_token_cookie', '', expires=0)
        return resp

    @app.route('/apidocs')
    @jwt_required()
    def protected_apidocs():
        return redirect('/apidocs/index.html')
