from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot_token = '6251146419:AAG71SUf4_r6kNeVYv-AMTKtfKV8N_3hmGo'
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# List of starter Pokemon
starter_pokemon = ["Bulbasaur", "Charmander", "Squirtle"]

# Dictionary to store user's chosen starter Pokemon
users_pokemon = {}

# Handler for /start command
def start(update, context):
    user_id = update.effective_user.id
    context.bot.send_message(chat_id=user_id, text="Welcome to the Pokemon world! Choose your starter Pokemon.")

    # Display starter Pokemon options
    options = "\n".join([f"{index + 1}. {pokemon}" for index, pokemon in enumerate(starter_pokemon)])
    context.bot.send_message(chat_id=user_id, text=options)

# Handler for /choose command
def choose(update, context):
    user_id = update.effective_user.id
    try:
        choice = int(context.args[0]) - 1
        chosen_pokemon = starter_pokemon[choice]

        users_pokemon[user_id] = chosen_pokemon
        context.bot.send_message(chat_id=user_id, text=f"Congratulations! You chose {chosen_pokemon} as your starter Pokemon.")
    except (ValueError, IndexError):
        context.bot.send_message(chat_id=user_id, text="Invalid choice. Please select a number from the list.")

# Handler for /pokemon command to display the user's chosen starter Pokemon
def my_pokemon(update, context):
    user_id = update.effective_user.id
    if user_id in users_pokemon:
        chosen_pokemon = users_pokemon[user_id]
        context.bot.send_message(chat_id=user_id, text=f"Your starter Pokemon is: {chosen_pokemon}")
    else:
        context.bot.send_message(chat_id=user_id, text="You haven't chosen a starter Pokemon yet.")

# Handler for random wild Pokemon encounter
def wild_encounter(update, context):
    user_id = update.effective_user.id
    if user_id in users_pokemon:
        chosen_pokemon = users_pokemon[user_id]

        # Simulate a wild Pokemon encounter
        wild_pokemon = random.choice(["Pidgey", "Rattata", "Caterpie", "Weedle", "Spearow"])

        context.bot.send_message(chat_id=user_id, text=f"A wild {wild_pokemon} appeared!")

        # You can implement further logic for Pokemon battles and capturing here
    else:
        context.bot.send_message(chat_id=user_id, text="You need to choose a starter Pokemon first.")

# Add handlers to the dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("choose", choose, pass_args=True))
dispatcher.add_handler(CommandHandler("pokemon", my_pokemon))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, wild_encounter))

# Start the bot
updater.start_polling()
updater.idle()
