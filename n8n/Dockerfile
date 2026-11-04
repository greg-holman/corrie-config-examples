FROM n8nio/n8n:2.46.6

# The n8n image has no curl program (its curl library is there), and the launcher needs one.
COPY --from=curlimages/curl:8.17.0 /usr/bin/curl /usr/local/bin/curl
ADD --chown=node:node https://config.corrie.io/launch.sh /home/node/launch.sh

# Keep the last settings that loaded on the n8n data volume, so n8n can still start if
# Corrie can't be reached when the container restarts.
ENV CORRIE_CONFIG_CACHE=/home/node/.n8n/corrie-settings.env

# The launcher loads the settings, then runs n8n through the image's own entrypoint, and
# restarts it within 60 seconds of a save.
ENTRYPOINT ["tini", "--", "sh", "/home/node/launch.sh", "--watch", "60", "--", "/docker-entrypoint.sh"]
