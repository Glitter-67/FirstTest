import discord
from discord.ext import commands
import asyncio
import os
import checkweb
import random
# Discordボットのトークンを環境変数から取得、または直接記述
TOKEN = os.getenv('DISCORD_BOT_TOKEN') # 環境変数から取得する場合
if TOKEN is None:
    print("エラー: DISCORD_BOT_TOKEN 環境変数が設定されていません。")
    print("ボットを起動できません。")
    exit(1) # プログラムを終了

# Intentsの設定
# デフォルトIntentsに加えて、MESSAGE_CONTENT Intentを有効にする必要があります
intents = discord.Intents.default()
intents.message_content = True # メッセージの内容を読み取るために必要

# クライアント（ボット）のインスタンスを作成
#client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

# ボットが起動したときに実行されるイベント
@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user}')

@bot.command()


async def rate(my_content):
    
    await my_content.send("プレイヤー名を入力してください。")

    
    def check(m):
        return m.author == my_content.author and m.channel == my_content.channel and m.author != bot.user

    try:
        msg = await bot.wait_for('message', check=check, timeout=10.0)
        await my_content.send(f"プレイヤー名: {msg.content} を受け付けました。")
    except asyncio.TimeoutError:
        await my_content.send("タイムアウト")
        return
    rates = checkweb.getRate(msg.content)
    await my_content.send("現在レート" + rates[0])
    await my_content.send("最高レート" + rates[1])



#メッセージが送信されたときに実行されるイベント

@bot.event
async def on_message(message):
    # ボット自身のメッセージには反応しないようにする
    if message.author == bot.user:
        return

    message_list = [
        "お呼びですよ！",
        "お呼びですにょ。"
    ]
    w = [100,1]
    bot_message = random.choices(message_list, weights = w)[0]

    #botメッセージの送信
    if 'たいぼ' in message.content:
        await message.channel.send(f'<@&{958916165479047209}>{bot_message}')
    elif '対募' in message.content:
        await message.channel.send(f'<@&{958916165479047209}>{bot_message}')
    elif '募集' in message.content:
        await message.channel.send(f'<@&{958916165479047209}>{bot_message}')

    await bot.process_commands(message) 
    

# ボットを実行

bot.run(TOKEN)

