import time

from flask import Flask
from opentracing import Tracer
from prometheus_client import Histogram, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from sample import counter

app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

c = counter.Counter()
h = Histogram("request_latency_seconds", "description...", ["endpoint"])

tracer = Tracer("app")


@app.route("/")
def get_counter():
    return f"{c.val}"


@app.route("/inc/")
def inc_count():
    c.inc()
    return f"{c.val}"


@app.route("/dec/")
def dec_count():
    with tracer.start_active_span(
        "dec_count_trace",
        tags={
            "tagkey": "tagvalue",
        },
    ):
        c.dec()
    return f"{c.val}"


@app.route("/long/")
def long():
    with h.labels(endpoint="long").time():
        time.sleep(3)
    return "done!"
