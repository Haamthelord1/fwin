import telebot 
import time 
import random
TOKEN = "5584666113:AAEZINo02AaeIB8-6UTW9i2V0znA_ZqRBlc"
bot = telebot.TeleBot(TOKEN) 
def send_image():
 a = random.randint(0,1)
 captions = ("🔴 Join Red On FastParity \n✋ Always Use Triple_Investment Method To Be In Profit\n🔸️Share It To Your Friends \n\nAnd Start Earning Now!|\n\nIt's Just An Ai Prediction, Follow At Your Own Risk!", "🟢 Join Green On FastParity \n✋ Always Use Triple_Investment Method To Be In Profit\n🔸️Share It To Your Friends \n\nAnd Start Earning Now! It's Just An Ai Prediction, Follow At Your Own Risk!") 
 with open(f"{a}.png", "rb") as file: bot.send_photo(-1001497946440, file, captions[a])

while True:
 send_image()
 time.sleep(1*30)
