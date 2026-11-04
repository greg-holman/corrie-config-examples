FROM python:3.12-slim

# The launcher needs curl. It fetches the settings, then starts the app with them.
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN curl -fsSLo /app/launch.sh https://config.corrie.io/launch.sh
COPY app.py /app/app.py

# A fixed non-root user, so the pod's runAsNonRoot check can verify it.
RUN useradd --uid 10001 --create-home app
USER 10001

EXPOSE 8000
CMD ["sh", "/app/launch.sh", "--watch", "60", "--", "python", "-u", "/app/app.py"]
