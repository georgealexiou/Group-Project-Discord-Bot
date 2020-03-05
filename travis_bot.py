import discord,asyncio,os
from discord.ext import commands
import checkTravis as travis
from datetime import date

from multiprocessing import Process

import imaplib, email
import time
import datetime as dt
from os import path
from datetime import timezone

################## DISCORD BOT #########################################3

def run():
    print ('Bot up and running')

bot = commands.Bot(command_prefix = '!')
<<<<<<< Updated upstream
=======
id = bot.get_guild(684446737313955871)
channel = bot.get_channel(685057313026867210)
>>>>>>> Stashed changes

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def check_travis(ctx):
    await ctx.send('Live fetching - Active')
    while True:
        print(temp.ready)
        if temp.ready is True:
            if temp.passed:
                await ctx.send('Your build has Passed')
            else:
                await ctx.send('Your build has Failed')
            temp.ready = False
        time.sleep(1)

####################### EMAIL ##########################################
class Mail:
    def __init__(self):
        with open('details.txt') as f:    
            details = f.read().splitlines()
            f.close()

        self.user = details[0]
        self.password = details[1]
        self.imap = 'imap.gmail.com'

        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.ready = False
        self.passed = False

    def check(self):
        self.mail.login(self.user,self.password)
        while True:
            self.mail.select('INBOX')
            unread = self.mail.search(None,'UnSeen')[1][0]
            if (unread == b''):
                print('Nothing new')
            else:
                result,data = self.mail.fetch(unread,'(RFC822)')
                raw = email.message_from_bytes(data[0][1])
                print(str(self.get_body(raw)))
                string_message = str(self.get_body(raw))

                if 'Software-Engineering-Group-Project' in string_message:
                    self.parse_email(str(self.get_body(raw)))

            time.sleep(5)

    def parse_email(self,contents):
        status = ''
        if 'errored' in contents:
            print('errored')
            self.ready = True
            self.passed = False
        elif 'passed' in contents:
            print('passed')
            self.ready = True
            self.passed = False

    def get_body(self,msg):
        if msg.is_multipart():
            return self.get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None,True)
        
####################### THREADING ########################################
def run_bot():
    with open('token.txt') as f:    
        token = f.read().splitlines()[0]
        f.close()
    bot.run(token)

def run_mail():
    temp.check()

temp = Mail()

<<<<<<< Updated upstream
bot.run('')
=======
if __name__ == '__main__':
    p1 = Process(target = run_bot)
    p2 = Process(target = run_mail)
    p1.start()
    p2.start()
>>>>>>> Stashed changes
