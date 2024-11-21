# Uptime Bot

The Uptime Bot is designed to monitor server availability by periodically sending GET requests to a specified URL. This ensures that the server remains active and helps in identifying any downtime or service interruptions. The bot operates at user-defined intervals, allowing for customizable monitoring based on the specific needs of the server.

## Requirements

- Docker Desktop (or just the engine is enough)

## Usage

1. Create a `.env` file and add the following variables

   ```.env
   SLEEP_TIME=180    # 3 minutes or whatever interval you want
   URL=https://example.com/health   # or whatever endpoint you want to check
   ```

2. On your terminal run `docker compose up`
   - You can add the `-d` flag to run the bot on detached mode
   - You can add the `--build` flag to rebuild the image before bringing it up

To see the logs, run `docker logs <specify the name of the container>`
