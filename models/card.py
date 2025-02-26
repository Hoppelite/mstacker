from uuid import UUID
from datetime import datetime
from typing import List
from util import nested_dataclass

@nested_dataclass
class ImageUris:
  small: str
  normal: str
  large: str
  png: str
  art_crop: str
  border_crop: str

@nested_dataclass
class Legalities:
  standard: str
  future: str
  historic: str
  timeless: str
  gladiator: str
  pioneer: str
  explorer: str
  modern: str
  legacy: str
  pauper: str
  vintage: str
  penny: str
  commander: str
  oathbreaker: str
  standardbrawl: str
  brawl: str
  alchemy: str
  paupercommander: str
  duel: str
  oldschool: str
  premodern: str
  predh: str

@nested_dataclass
class Preview:
  source: str
  source_uri: str
  previewed_at: datetime

@nested_dataclass
class Prices:
  usd: str
  usd_foil: str
  usd_etched: str
  eur: str
  eur_foil: str
  tix: str

@nested_dataclass
class PurchaseUris:
  tcgplayer: str
  cardmarket: str
  cardhoarder: str

@nested_dataclass
class RelatedUris:
  gatherer: str
  tcgplayer_infinite_articles: str
  tcgplayer_infinite_decks: str
  edhrec: str

@nested_dataclass
class RelatedCard:
  object: str
  id: UUID
  component: str
  name: str
  type_line: str
  uri: str

@nested_dataclass
class Card:
  object: str
  all_parts: List[RelatedCard]
  id: UUID
  oracle_id: UUID
  multiverse_ids: List[int]
  mtgo_id: int
  arena_id: int
  tcgplayer_id: int
  cardmarket_id: int
  name: str
  lang: str
  released_at: datetime
  uri: str
  scryfall_uri: str
  layout: str
  highres_image: bool
  image_status: str
  image_uris: ImageUris
  mana_cost: str
  cmc: int
  type_line: str
  oracle_text: str
  power: int
  toughness: int
  colors: List[str]
  color_identity: List[str]
  keywords: List[str]
  legalities: Legalities
  games: List[str]
  reserved: bool
  game_changer: bool
  foil: bool
  nonfoil: bool
  finishes: List[str]
  oversized: bool
  promo: bool
  reprint: bool
  variation: bool
  set_id: UUID
  set: str
  set_name: str
  set_type: str
  set_uri: str
  set_search_uri: str
  scryfall_set_uri: str
  rulings_uri: str
  prints_search_uri: str
  collector_number: int
  digital: bool
  rarity: str
  card_back_id: UUID
  artist: str
  artist_ids: List[UUID]
  illustration_id: UUID
  border_color: str
  frame: int
  frame_effects: List[str]
  security_stamp: str
  full_art: bool
  textless: bool
  booster: bool
  story_spotlight: bool
  edhrec_rank: int
  penny_rank: int
  preview: Preview
  prices: Prices
  related_uris: RelatedUris
  purchase_uris: PurchaseUris
