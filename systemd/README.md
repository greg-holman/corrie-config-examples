# systemd service

Run an app as a systemd service that loads its settings from Corrie Config, restarts within a minute of a save, keeps the key out of the unit file and still starts from a cached copy offline. Complete, tested example.

The full walkthrough, with the commands to run and what you should see, is in the guide: https://config.corrie.io/docs/systemd

Files in this folder:

- `app.py`
- `corrie-example.service`

To try it you need a Corrie Config key for an environment. You can make one on the free plan at https://config.corrie.io/signup?ref=config-examples
