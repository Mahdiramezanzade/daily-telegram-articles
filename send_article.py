"""Send a daily science article to a Telegram chat.

This script fetches the latest article from ScienceDaily's RSS feed and sends
the title, summary, and link to a Telegram chat using a bot token.
"""

import os
import re
from html import unescape
from typing import Optional

import feedparser
import requests


BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


def get_latest_article() -> Optional[dict]:
    """Retrieve the newest article from ScienceDaily's RSS feed."""

    rss_url = "https://www.sciencedaily.com/rss/top/science.xml"
    resp = requests.get(rss_url, timeout=10)
    feed = feedparser.parse(resp.content)
    if not feed.entries:
        return None

    entry = feed.entries[0]
    summary = re.sub("<[^>]+>", "", entry.get("summary", "")).strip()
    summary = unescape(summary)

    return {
        "title": entry.get("title", "Untitled"),
        "link": entry.get("link", ""),
        "summary": summary,
    }


def send_message(text: str) -> None:
    """Send a message to the configured Telegram chat."""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False,
    }

    resp = requests.post(url, data=params, timeout=10)
    print(resp.json())


def main() -> None:
    article = get_latest_article()
    if not article:
        send_message("Failed to fetch today's article.")
        return

    message = (
        f"📘 *Daily Science Article*\n\n"
        f"📰 *Title:* _{article['title']}_\n"
        f"🔗 [Read the full article]({article['link']})\n\n"
        f"📝 *Summary:* {article['summary']}"
    )

    # Telegram messages are limited to 4096 characters.
    message = message[:4000]
    send_message(message)


if __name__ == "__main__":
    main()

