# Multi-Site News Summarizer with Optional Notifications

Scrapes multiple news sites, summarizes with OpenAI, stores in Postgres, and optionally sends via Email/Telegram.

## Setup
1. Add URLs and selectors in `sites_config.py`.
2. Set environment variables:
   - `OPENAI_API_KEY`
   - `DATABASE_URL` (Railway Postgres plugin)
   - Optional email vars: `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `TO_EMAIL`
   - Optional Telegram vars: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`
3. Install deps:
   ```bash
   uv pip install -r requirements.txt
