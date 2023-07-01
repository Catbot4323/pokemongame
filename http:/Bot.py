from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# Replace with your own Telegram Bot Token
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# List of starter Pokémon
starter_pokemon = ["Bulbasaur", "Charmander", "Squirtle"]

# Start command handler
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    message = (
        f"Hello, {user.first_name}!\n"
        "Welcome to the Pokémon World! Choose your starter Pokémon:\n"
    )

    # Create the list of buttons for starter Pokémon selection
    keyboard = [
        [InlineKeyboardButton(pokemon, callback_data=pokemon)] for pokemon in starter_pokemon
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the selection menu
    update.message.reply_text(message, reply_markup=reply_markup)

# Callback query handler for starter Pokémon selection
def select_starter(update: Update, context: CallbackContext):
    query = update.callback_query
    user = update.effective_user
    selected_pokemon = query.data

    # Replace this with your logic for the starter Pokémon selection process
    # For example, you can save the user's selection to a database
    # and continue with the rest of your game logic

    query.answer(f"You've chosen {selected_pokemon} as your starter Pokémon!")

# Main function to run the bot
def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Register the handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(select_starter))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
    
