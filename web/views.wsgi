import sys

print('attempt')
# ***

path = '/var/www/html/catalog/web'
if path not in sys.path:
   sys.path.insert(0, path)

from views import app as application

application.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# def application(environ, start_response):
#     status = '200 OK'
#     output = tester.hi()

#     response_headers = [('Content-type', 'text/plain'),
#                         ('Content-Length', str(len(output)))]
#     start_response(status, response_headers)

#     return [output]

# sudo rm -rf /var/www/html/catalog/web
# sudo cp -r ~/catalog/ /var/www/html/

# var/www/html
