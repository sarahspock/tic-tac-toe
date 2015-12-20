from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from rest_api import app as backend
from client import app as frontend

# The API and the frontend are decoupled. This middleware combines two different
# applications to run on one port.

application = DispatcherMiddleware(frontend, {
    "/api": backend
})

if __name__ == "__main__":
    run_simple('localhost', 5000, application,
               use_reloader=True, use_debugger=True,
               use_evalex=True, threaded=True)
