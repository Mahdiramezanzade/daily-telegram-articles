# daily-telegram-articles

This project posts the latest article from ScienceDaily to a private Telegram
channel every day using GitHub Actions.

The workflow runs `send_article.py`, which fetches the newest item from
ScienceDaily's RSS feed and sends it via the Telegram Bot API. Set the
`TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` secrets in your repository to enable
the workflow.
