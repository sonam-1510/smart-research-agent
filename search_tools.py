import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

def search_google(query, num_results=5):
    params = {
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "engine": "google",
        "num": num_results
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    links = []

    for result in results.get("organic_results", []):
        title = result.get("title")
        snippet = result.get("snippet")
        link = result.get("link")
        links.append(f"Title: {title}\nSnippet: {snippet}\nURL: {link}\n")

    return "\n---\n".join(links)
