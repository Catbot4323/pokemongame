import requests
from telethon.sync import TelegramClient, events
import random

# Bot token (replace with your own)
BOT_TOKEN = '5867575325:AAHFnm-6poBB5UGv57T4R2I7saMybNWaGao'

# API ID and API hash (replace with your own)
API_ID = '2227210'
API_HASH = '5372738ac54c8940b091817ffb4b4e58'

# Create a TelegramClient instance
client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(pattern='/hunt'))
async def handle_hunt(event):
    if event.is_private:  # Only respond to private messages
        # Check if the message is from the user who initiated the command
        if event.sender_id == event.message.peer_id.user_id:
            # Generate a random Pokémon ID (between 1 and 898)
            pokemon_id = random.randint(1, 898)

            # Make a request to the PokéAPI to get information about the Pokémon
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
            if response.status_code == 200:
                pokemon_data = response.json()
                pokemon_name = pokemon_data['name']
                pokemon_images = []

                # Fetch high-resolution images from the Pokédex Sprites endpoint
                if 'sprites' in pokemon_data and 'other' in pokemon_data['sprites']:
                    sprites = pokemon_data['sprites']['other']
                    if 'official-artwork' in sprites:
                        official_artwork = sprites['official-artwork']
                        if 'front_default' in official_artwork:
                            pokemon_images.append(official_artwork['front_default'])

                # Send the hunted Pokémon's pictures and information as a message
                message = f"You encountered a wild {pokemon_name}!\n\n"
                for image_url in pokemon_images:
                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        image_bytes = image_response.content
                        await client.send_message(event.chat_id, message, file=image_bytes)

def main():
    # Start the client with the bot token
    client.start(bot_token=BOT_TOKEN)

    # Run the client until it's disconnected
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
