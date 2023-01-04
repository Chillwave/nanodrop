# Open the file in read-only mode
with open('readme.md', 'r') as file:
    # Read the contents of the file
    readme = file.read()

# Print the contents of the file to the console
print(readme)

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
