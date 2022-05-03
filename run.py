from app import create_connections, close_connections, get_flask_server

if __name__ == '__main__':
    app = get_flask_server()
    app.run()
