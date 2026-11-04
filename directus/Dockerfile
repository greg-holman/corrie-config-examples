FROM directus/directus:12.6.0

# The Directus image has no curl program, and the launcher needs one.
USER root
RUN apk add --no-cache curl
USER node
ADD --chown=node:node https://config.corrie.io/launch.sh /directus/launch.sh

# Keep the last settings that loaded on the database volume, so Directus can still start if
# Corrie can't be reached when the container restarts.
ENV CORRIE_CONFIG_CACHE=/directus/database/corrie-settings.env

# The launcher loads the settings, then runs the image's own start command (bootstrap, then
# pm2-runtime), and restarts it within 60 seconds of a save.
ENTRYPOINT ["sh", "/directus/launch.sh", "--watch", "60", "--", "node", "docker-entrypoint.cjs"]
