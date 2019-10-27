from telethon import TelegramClient, events, sync, client

# credentials
api_id = 1112802
api_hash = "8961da04758e6caaa8184dae5f9cc5da"
client = TelegramClient('anon', api_id, api_hash)
client.flood_sleep_threshold = 0


async def get_user_info():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is an User object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

async def send_message():
    await client.send_message('me', 'Check)')



# @client.on(events.NewMessage)
# async def reply_on_message(event):
#     if 'hello' in event.raw_text:
#         await event.reply('hi!')
#


@client.on(events.NewMessage('TextMe(HackMoscow)'))
async def get_audio(event):
    # print(event.message.to_dict())
    message = event.message
    if message.media is not None:
        await client.download_media(message=message)

client.start(phone='+79251286565', password='tikhon20telegram')
client.run_until_disconnected()

with client:
    # client.loop.run_until_complete(send_message())
    # client.loop.run_until_complete(new_message())
    client.loop.run_until_complete(get_audio())
