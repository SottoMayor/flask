def log_middleware(app):
    @app.before_request
    def in_request():
        print("[Aviso] Antes!")

    @app.after_request
    def out_request(response):
        print("[Aviso] Depois da request!")
        return response