FROM ghost:6

# The Ghost image has no curl program, and the launcher needs one.
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /var/lib/corrie && chmod 700 /var/lib/corrie
ADD https://config.corrie.io/launch.sh /usr/local/bin/launch.sh

# Ghost reads lowercase names with __ for each level (database__connection__host), so ask
# Corrie for the exact names. Keep the last settings that loaded in a root-only folder on its
# own volume, so Ghost can still start if Corrie can't be reached when the container restarts.
ENV CORRIE_CONFIG_NAMES=exact CORRIE_CONFIG_CACHE=/var/lib/corrie/settings.env

# The launcher loads the settings, then runs the image's own entrypoint, which hands Ghost to
# the node user, and restarts Ghost within 60 seconds of a save.
ENTRYPOINT ["sh", "/usr/local/bin/launch.sh", "--watch", "60", "--", "docker-entrypoint.sh"]
CMD ["node", "current/index.js"]
