from prometheus_fastapi_instrumentator import Instrumentator
...
"""
Код из main.py отвечающий за отдачу метрик для Prometheus.
"""

Instrumentator().instrument(app).expose(
    app,
    endpoint="/metrics",
    include_in_schema=False,
)