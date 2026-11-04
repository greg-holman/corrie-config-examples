# Corrie Config examples

Runnable examples for [Corrie Config](https://config.corrie.io/?ref=config-examples), which keeps an app's settings in one place and hands them to the app as plain environment variables when it starts.

Every folder here is the exact set of files used in one of the integration guides at https://config.corrie.io/docs, and we ran each of them against config.corrie.io before publishing the guide. The apps contain no Corrie code or client library. They read ordinary environment variables, and the launcher (`launch.sh`) fetches the settings, starts the app and, with `--watch`, restarts it when a setting is saved.

## Quick start

1. Sign up free at https://config.corrie.io/signup?ref=config-examples, create a project and save a few settings in its `production` environment.
2. Create a key for that environment.
3. Pick a folder below and follow its guide. For most of them it comes down to:

```bash
curl -fsSLo launch.sh https://config.corrie.io/launch.sh
export CORRIE_CONFIG_KEY=cfg_your_production_key
sh launch.sh --watch 60 -- <the command that starts your app>
```

Keep the key out of the repository. The examples read it from the environment, a `.env` file, a Kubernetes Secret or a CI secret.

## Examples

- [Node.js and Express](node-express/): Load an Express app's settings from Corrie Config with the launcher, and restart it automatically within a minute of a save. Complete, tested example. Guide: https://config.corrie.io/docs/node-express
- [Python and Flask](python-flask/): Load a Flask app's settings from Corrie Config with the launcher. Complete, tested example. Guide: https://config.corrie.io/docs/python-flask
- [Python and FastAPI](python-fastapi/): Run a FastAPI app under Uvicorn with its settings from Corrie Config, and restart it automatically within a minute of a save. Complete, tested example. Guide: https://config.corrie.io/docs/python-fastapi
- [Docker and Docker Compose](docker-compose/): Run a container that loads its settings from Corrie Config when it starts, restarts the app within a minute of a save, and still starts from a cached copy if Corrie can't be reached. Complete, tested example. Guide: https://config.corrie.io/docs/docker-compose
- [systemd service](systemd/): Run an app as a systemd service that loads its settings from Corrie Config, restarts within a minute of a save, keeps the key out of the unit file and still starts from a cached copy offline. Complete, tested example. Guide: https://config.corrie.io/docs/systemd
- [GitHub Actions](github-actions/): Load an environment's settings from Corrie Config in a GitHub Actions workflow, keep the key in a repository secret, and fail the job when a setting is missing. Complete, tested example. Guide: https://config.corrie.io/docs/github-actions
- [Next.js](nextjs/): Run a Next.js app with its settings from Corrie Config: server code reads them at request time under next start, the app restarts within a minute of a save, and NEXT_PUBLIC_ settings load at build time. Complete, tested example. Guide: https://config.corrie.io/docs/nextjs
- [Django](django/): Run a Django app under Gunicorn with its settings from Corrie Config: read them in settings.py, run migrations through the launcher and restart within a minute of a save. Complete, tested example. Guide: https://config.corrie.io/docs/django
- [Go](go/): Run a Go net/http service with its settings from Corrie Config: read them with os.Getenv at start, shut down cleanly on TERM and restart within a minute of a save. Complete, tested example. Guide: https://config.corrie.io/docs/go
- [.NET and ASP.NET Core](dotnet/): Run an ASP.NET Core app with its settings from Corrie Config: read them through builder.Configuration, use __ for configuration sections and restart within a minute of a save. Complete, tested example. Guide: https://config.corrie.io/docs/dotnet
- [Java and Spring Boot](spring-boot/): Run a Spring Boot app with its settings from Corrie Config: bind them to a validated @ConfigurationProperties record, run the jar through the launcher and restart within a minute of a save. Complete, tested example. Guide: https://config.corrie.io/docs/spring-boot
- [PHP and Laravel](laravel/): Run a Laravel app under php-fpm with its settings from Corrie Config: read them in a config file, rebuild the config cache on each start and restart within a minute of a save. Complete, tested example. Guide: https://config.corrie.io/docs/laravel
- [Ruby on Rails](rails/): Run a Rails app under Puma with its settings from Corrie Config: read them in an initializer, run migrations and the server through the launcher and restart within a minute of a save. Complete, tested example. Guide: https://config.corrie.io/docs/rails
- [Kubernetes](kubernetes/): Run an app on Kubernetes with its settings from Corrie Config: the key in a Secret, the launcher as the container command, a cached copy in a pod volume and restarts within a minute of a save. Complete, tested example. Guide: https://config.corrie.io/docs/kubernetes
- [Vite, React and static frontends](vite/): Build a Vite app (React, Vue, Svelte or plain JavaScript) with its settings from Corrie Config: which settings end up in the built files, how to build with the launcher and when to build again. Complete, tested example. Guide: https://config.corrie.io/docs/vite
- [Umami analytics](umami/): Run self-hosted Umami with its settings from Corrie Config: the official image with the launcher added, the database password and APP_SECRET kept out, and Umami restarted within a minute of a save. Tested example. Guide: https://config.corrie.io/docs/umami
- [n8n workflow automation](n8n/): Run self-hosted n8n with its settings from Corrie Config: the official image with curl and the launcher added, N8N_ENCRYPTION_KEY kept out, and n8n restarted within a minute of a save. Tested example. Guide: https://config.corrie.io/docs/n8n
- [Directus headless CMS](directus/): Run self-hosted Directus with its settings from Corrie Config: the official image with curl and the launcher added, SECRET and the admin password kept out, and Directus restarted within a minute of a save. Tested example. Guide: https://config.corrie.io/docs/directus

## Questions

Email support@corrie.io with the example name and what you see. Please never include the key itself.

## License

MIT, see [LICENSE](LICENSE).
