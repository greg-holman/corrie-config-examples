FROM python:3.12-slim

# The launcher needs curl. It fetches the settings, then starts the app with them.
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN curl -fsSLo /app/launch.sh https://config.corrie.io/launch.sh
COPY app.py /app/app.py

# Run as a normal user. /data keeps the last settings that loaded, so the app can still
# start if Corrie can't be reached when the container restarts.
RUN useradd --create-home app && mkdir /data && chown app /data
USER app
ENV CORRIE_CONFIG_CACHE=/data/settings.env

EXPOSE 8000
CMD ["sh", "/app/launch.sh", "--watch", "60", "--", "python", "-u", "/app/app.py"]
