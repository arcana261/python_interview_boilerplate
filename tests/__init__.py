from sanic import Sanic

#from core.extentions.exceptions import blueprint as ext_exceptions
#from core.extentions.middlewares import blueprint as ext_middlewares

from apps.myapp import blueprint as myapp

def build_full_app(settings={}):
    """Build Sanic Full App
    Mirroring main.py
    Args:
        settings = A dictionary of application settings (optional)
    Returns:
        A sanic app
    """
    app = Sanic('test')

    # only updating settings if given settings
    # has values
    if isinstance(settings, dict):
        if len(settings.keys()) >= 1:
            app.config.update(settings)

    #app.blueprint(ext_exceptions)
    #app.blueprint(ext_middlewares)
    app.blueprint(myapp, url_prefix='/')

    return app