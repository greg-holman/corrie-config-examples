# n8n workflow automation

Run self-hosted n8n with its settings from Corrie Config: the official image with curl and the launcher added, N8N_ENCRYPTION_KEY kept out, and n8n restarted within a minute of a save. Tested example.

The full walkthrough, with the commands to run and what you should see, is in the guide: https://config.corrie.io/docs/n8n

Files in this folder:

- `Dockerfile`
- `compose.yaml`

To try it you need a Corrie Config key for an environment. You can make one on the free plan at https://config.corrie.io/signup?ref=config-examples
