# news_bot.py
import requests
import sys
from config import NEWS_API_KEY

def search_crypto_news(query):
    """
    A function for searching for news about crypto projects using NewsAPI.
    
    Args:
        query (str): User's search query (for example, "Bitcoin", "Ethereum DeFi")
    
    Returns:
        list: List of dictionaries with information about articles, or None if an error occurs.
    """

    # The base URL for a request to the Everything endpoint of the NewsAPI
    url = "https://newsapi.org/v2/everything"
    
    # Request Parameters
    params = {
        'q': query,          # Search query
        'sortBy': 'publishedAt', # Sort by publication date (newest first)
        'language': 'en',    # Article language (Standard EU)
        'pageSize': 10,      # Number of results (max. 100 on the free plan)
        'apiKey': NEWS_API_KEY
    }
    
    try:
        print(f"[+] We are looking for news on request: '{query}'...")
        response = requests.get(url, params=params)
        response.raise_for_status()  # Throws an exception for the codes 4xx/5xx
        
        data = response.json()
        
        # Checking the response status from the API
        if data['status'] == 'ok':
            return data['articles']
        else:
            print(f"[-] Error in the API response: {data.get('message', 'Unknown error')}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Network error when requesting NewsAPI: {e}")
        return None
    except Exception as e:
        print(f"[-] Unexpected error: {e}")
        return None

def display_news(articles):
    """
    A feature for beautifully displaying found news.
    
    Args:
        articles (list): The list of articles received from the API.
    """
    if not articles:
        print("Unfortunately, nothing was found for your request.")
        return
    
    print(f"\n--- Results found: {len(articles)} ---\n")
    
    for idx, article in enumerate(articles, 1):
        title = article.get('title', 'Untitled')
        source = article.get('source', {}).get('name', 'Unknown source')
        url = article.get('url', '#')
        published_at = article.get('publishedAt', 'Date unknown')[:10] # We cut off the time, leave the date
        
        print(f"{idx}. {title}")
        print(f"   A source: {source}")
        print(f"   Date: {published_at}")
        print(f"   Link: {url}")
        print()

def main():
    # Checking whether a command-line argument is passed
    if len(sys.argv) < 2:
        print("Usage: python news_bot.py <search query>")
        print('Example: python news_bot.py "Bitcoin ETF"')
        sys.exit(1)
    
    # Combine all the arguments into a single query string
    search_query = " ".join(sys.argv[1:])
    
    # Looking for news
    articles = search_crypto_news(search_query)
    
    # Showing the results
    if articles is not None:
        display_news(articles)

if __name__ == "__main__":
    main()