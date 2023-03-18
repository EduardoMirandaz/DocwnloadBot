import logging
from PIL import Image
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import requests

CHAVE_BOT = open('api_key.txt', 'r').read()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def processarImagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id_foto = update.message.photo[-1].file_id
    print(id_foto)
    caminho_da_foto_no_servidor = requests.get("https://api.telegram.org/bot"+CHAVE_BOT+"/getFile?file_id="+id_foto)
    print(caminho_da_foto_no_servidor)

    # imagem_transcrita = pytesseract.image_to_string( foto_baixada, lang='por')
    await context.bot.send_message(chat_id=update.effective_chat.id, text="\nRECEBI SUA IMAGEM\n")

if __name__ == '__main__':
    application = ApplicationBuilder().token(CHAVE_BOT).build()
    
    inicio_handler = CommandHandler('start', start)
    imagem_handler = MessageHandler(filters.PHOTO, processarImagem)

    
    application.add_handler(inicio_handler)
    application.add_handler(imagem_handler)
    application.run_polling()