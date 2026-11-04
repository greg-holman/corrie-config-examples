FROM ghcr.io/umami-software/umami:3.4.1

# The official image already has curl. Add the launcher next to Umami's own start script.
USER root
RUN curl -fsSLo /app/launch.sh https://config.corrie.io/launch.sh \
    && mkdir /data && chown nextjs /data
USER nextjs

# /data keeps the last settings that loaded, so Umami can still start if Corrie can't be
# reached when the container restarts.
ENV CORRIE_CONFIG_CACHE=/data/settings.env

# The launcher loads the settings, then runs Umami's own start script (database check,
# migrations, then the server), and restarts it within 60 seconds of a save.
CMD ["sh", "/app/launch.sh", "--watch", "60", "--", "sh", "scripts/start-docker.sh"]
