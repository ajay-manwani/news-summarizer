SITES = [
    {
        "name": "Economic Times",
        "base_url": "https://economictimes.indiatimes.com",
        "articles": [
            "https://economictimes.indiatimes.com/news/sports/bangladesh-vs-sri-lanka-asia-cup-2025-t20-match-live-streaming-when-and-where-to-watch-the-fifth-game/articleshow/123868535.cms",
            "https://economictimes.indiatimes.com/wealth/tax/seven-situations-when-gifts-received-by-an-individual-are-free-from-income-tax/articleshow/123866052.cms"
        ],
        # ET articles have main text in <p> tags inside the main content area
        "content_selector": "p"
    },
    # {
    #     "name": "BBC",
    #     "base_url": "https://www.bbc.com",
    #     "articles": [
    #         "https://www.bbc.com/news/world-asia-68386587",
    #         "https://www.bbc.com/news/business-68385421"
    #     ],
    #     "content_selector": "div[data-component='text-block'] p"
    # }
]
