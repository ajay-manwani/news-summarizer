from sites_config import SITES
from scraper import scrape_page
from summarizer import summarize_text
from storage import init_db, save_summary
from notifier import send_email, send_telegram

def main():
    init_db()
    all_summaries = []

    for site in SITES:
        for url in site["articles"]:
            print(f"Fetching: {url}")
            try:
                article_text = scrape_page(url, site["content_selector"])
                summary = summarize_text(article_text)
                print(summary)
                save_summary(site["name"], url, summary)
                all_summaries.append(f"{site['name']} - {url}\n{summary}\n")
                print(f"Saved summary for {url}")
            except Exception as e:
                print(f"Error processing {url}: {e}")

    if False:  # Change to True to enable notifications
        combined = "\n\n".join(all_summaries)
        send_email("Daily News Summaries", combined)
        send_telegram(combined)

if __name__ == "__main__":
    main()
