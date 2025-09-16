from unicodedata import name
from unittest import result
from flask import Flask, jsonify, session, redirect, url_for
from authlib.integrations.flask_client import OAuth

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

    oauth = OAuth(app)

    oauth.register(
        name='oidc',
        authority='https://cognito-idp.eu-north-1.amazonaws.com/eu-north-1_E4LqxitPq',
        client_id='7k0q9pm4hbgbijjr45ldtoa7d4',
        client_secret='<client secret>',
        server_metadata_url='https://cognito-idp.eu-north-1.amazonaws.com/eu-north-1_E4LqxitPq/.well-known/openid-configuration',
        client_kwargs={'scope': 'openid email'}
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
        # Alternate option to redirect to /authorize
        # redirect_uri = url_for('authorize', _external=True)
        # return oauth.oidc.authorize_redirect(redirect_uri)
        return oauth.oidc.authorize_redirect('https://13.62.126.132:5000/apidocs')
    
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
