from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.route('/')
def hello():
    """Return a friendly greeting.

    Query Parameters:
        name (str): The name to greet. Defaults to 'World'.

    Returns:
        str: A greeting message.
    """
    name = request.args.get('name', 'World').strip()
    if not name:
        return jsonify({'error': 'Name parameter cannot be empty'}), 400
    return f'Hello, {name}!'

@app.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

# Added ProxyFix middleware - Better support for running behind reverse proxies
#Input validation - Added .strip() and empty check for the name parameter
#Error handling - Returns a 400 Bad Request for empty names
#Added JSON support - Imported jsonify for consistent API responses
#Added health check endpoint - Standard practice for monitoring
#Improved docstrings - Better documentation for the endpoints
#Production-ready run configuration:
#Set debug=False for production
#Explicit host and port
#Listen on all interfaces (0.0.0.0)
#ecurity - Basic input sanitization with .strip()
#API consistency - Health check returns JSON like a proper API
#For even more robust production use, you might want to add:

#Rate limiting
#Proper logging configuration
#Environment variable configuration
#CORS support
#Request size limits
#More comprehensive error handling