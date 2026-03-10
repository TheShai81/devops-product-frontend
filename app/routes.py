from app import app
from flask import render_template, request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

# https://prometheus.github.io/client_python/

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency in seconds',
    ['method', 'endpoint']
)

@app.before_request
def before_request():
    request._start_time = time.time()

@app.after_request
def after_request(response):
    endpoint = request.path
    method = request.method
    status = response.status_code

    REQUEST_COUNT.labels(
        method=method,
        endpoint=endpoint,
        status=status
    ).inc()

    if hasattr(request, '_start_time'):
        REQUEST_LATENCY.labels(
            method=method,
            endpoint=endpoint
        ).observe(time.time() - request._start_time)

    return response

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route("/")
def index():
    return render_template("index.html")
