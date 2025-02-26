
import os
import requests
import time

from models.card import Card

BASE_URL = "https://mtgsingles.co.nz:14567/"
API_LIMIT = 1 # 1 per second
DEFAULT_HEADERS = {
  "Accept": "application/json"
}

last_request = 0

def url_for(*url):
  return os.path.join(BASE_URL, *url)

def with_limit(func):
  def wrapper(*args, **kwargs):
    global last_request
    time_since_last = time.time() - last_request
    if time_since_last < API_LIMIT:
      time.sleep(API_LIMIT - time_since_last)
    response = func(*args, **kwargs)
    last_request = time.time()
    return response
  return wrapper

def get(url, params=None):
  response = with_limit(requests.get)(url, headers=DEFAULT_HEADERS, params=params)
  response.raise_for_status()
  return response.json()

def post(url, data=None):
  response = with_limit(requests.post)(url, headers=DEFAULT_HEADERS, json=data)
  response.raise_for_status()
  return response.json()

def search_stores(name: str, page = 1, page_size = 20, country = 1) -> any:
  url = url_for("MtgSingle")
  params = {"query": name, "page": page, "pageSize": page_size, "Country": country}
  response = get(url, params)
  return response

def search_stores_by_card(card: Card) -> any:
  return search_stores(card.name)

