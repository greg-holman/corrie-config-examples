# Docker and Docker Compose

Run a container that loads its settings from Corrie Config when it starts, restarts the app within a minute of a save, and still starts from a cached copy if Corrie can't be reached. Complete, tested example.

The full walkthrough, with the commands to run and what you should see, is in the guide: https://config.corrie.io/docs/docker-compose

Files in this folder:

- `Dockerfile`
- `app.py`
- `compose.yaml`

To try it you need a Corrie Config key for an environment. You can make one on the free plan at https://config.corrie.io/signup?ref=config-examples
