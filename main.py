import api.cards as card_api

# Example of how to use the card_api
# The search is fuzzy, but it will 404 if it isn't specific enough
card = card_api.get_card_by_name("Talion the kindly")
