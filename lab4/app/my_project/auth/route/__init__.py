from unicodedata import name
from unittest import result
from flask import Flask, jsonify, session, redirect, url_for
from authlib.integrations.flask_client import OAuth
import os

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

    app.secret_key = os.urandom(24)
    oauth = OAuth(app)

    oauth.register(
        name='oidc',
        authority='https://cognito-idp.eu-north-1.amazonaws.com/eu-north-1_1Kdpw4lCk',
        client_id='4isd6qjb07rnrn70dsqktuirfa',
        client_secret='5ab1ttrbiefgf54m6jf3kcbpccb5m8v4gmh6fr2i8q81iacsd3o',
        server_metadata_url='https://cognito-idp.eu-north-1.amazonaws.com/eu-north-1_1Kdpw4lCk/.well-known/openid-configuration',
        client_kwargs={'scope': 'phone openid email'}
    )

    @app.route('/')
    def index():
        user = session.get('user')
        if user:
            return  f'Hello, {user["email"]}. <a href="/logout">Logout</a>'
        else:
            return f'Welcome! Please <a href="/login">Login</a>.'
        
    @app.route('/login')
    def login():
        return oauth.oidc.authorize_redirect('http://localhost:5000/apidocs')
        
    
    @app.route('/authorize')
    def authorize():
        token = oauth.oidc.authorize_access_token()
        user = token['userinfo']
        session['user'] = user
        return redirect(url_for('index'))

    @app.route('/logout')
    def logout():
        session.pop('user', None)
        return redirect(url_for('index'))