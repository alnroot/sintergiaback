#!/bin/sh
echo "Starting application..."
uvicorn app.main:app --host 0.0.0.0 --port 8002 --workers 2

# fly.toml
app = "sintergia"

[build]
  dockerfile = "Dockerfile"

[env]
  PORT = "8002"

[[services]]
  internal_port = 8002
  protocol = "tcp"
  
  [[services.ports]]
    force_https = true
    handlers = ["http"]
    port = 80

  [[services.ports]]
    handlers = ["tls", "http"]
    port = "443"

  [[services.tcp_checks]]
    grace_period = "30s"
    interval = "15s"
    restart_limit = 6
    timeout = "2s"