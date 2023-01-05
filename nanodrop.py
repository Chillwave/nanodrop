import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

# Open the file in read-only mode, with a default value of an empty string
# in case the file does not exist
try:
    with open('art.txt', 'r') as file:
        # Read the contents of the file
        readme = file.read()
except FileNotFoundError:
    readme = ''

# Print the contents of the file to the console
print(readme)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
