from api import handler
from models.card import Card
from uuid import UUID

def get_card_by_name(name: str) -> Card:
  url = handler.url_for("cards/named")
  params = {"fuzzy": name}
  response = handler.get(url, params)
  return Card(**response)

def get_rulings_for_card(card: Card) -> any:
  url = card.rulings_uri
  response = handler.get(url)
  return response

def get_card_by_id(id: UUID) -> Card:
  url = handler.url_for("cards", id)
  response = handler.get(url)
  return Card(**response)
