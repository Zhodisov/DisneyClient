



#                https://safemarket.xyz | https://safemarket.xyz/discord
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#  | | ____     _     _____  _____      __  __     _     ____   _  __ _____  _____ | |  
#  | |/ ___|   / \   |  ___|| ____|    |  \/  |   / \   |  _ \ | |/ /| ____||_   _|| |  
#  | |\___ \  / _ \  | |_   |  _|      | |\/| |  / _ \  | |_) || ' / |  _|    | |  | |  
#  | | ___) |/ ___ \ |  _|  | |___     | |  | | / ___ \ |  _ < | . \ | |___   | |  | |  
#  | ||____//_/   \_\|_|    |_____|    |_|  |_|/_/   \_\|_| \_\|_|\_\|_____|  |_|  | |  
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#                               https://github.com/Jodis974                           



from discord import Embed, Intents
from discord.ext import commands
from typing import Dict, Optional
import discord
import infrastructure
import os

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True

class Bot(commands.Bot):
    def __init__(self, command_prefix="!"):
        super().__init__(command_prefix, intents=intents)

        self.discord_names = None
        self.log_channel = None
        self.log_channel2 = None
        self.priv_channel = None

        self.add_listener(self.ready, "on_ready")
        self.remove_command("help")

        print("[Discord] Bot is initializing...")

    async def on_ready(self):
        print("[Discord] Bot is ready!")
        print(f"[Discord] Logged in as {self.user.name} ({self.user.id})")
        # Call the load_cogs method using create_task
        self.loop.create_task(self.load_cogs())

    async def load_cogs(self):
        # Load extensions (cogs) here
        cogs_path = os.path.join(os.path.dirname(__file__), "cogs")
        if not os.path.isdir(cogs_path):
            raise Exception("`cogs` dir from package `discordbot` not found")

        for file in os.listdir(cogs_path):
            print(f"[Discord] Loading extension: {file}")
            if not file.startswith("_") and file.endswith(".py"):
                try:
                    await self.load_extension(f"discordbot.cogs.{file[:-3]}")
                except Exception as e:
                    print(f"[Discord] Failed to load extension {file}: {e}")

    async def ready(self):
        self.discord_names = [str(await self.fetch_user(_id)) for _id in (infrastructure.config["discord_admins"])]
        self.log_channel = self.get_channel(infrastructure.config["discord_log_channel"])
        self.log_channel2 = self.get_channel(infrastructure.config["discord_log_channel2"])
        self.priv_channel = self.get_channel(infrastructure.config["discord_priv_channel"])
        print("[Discord] Ready")
        print(f"[Discord] Log channels: {self.log_channel}, {self.log_channel2}, {self.priv_channel}")

    async def log(self, method: str, response: Dict, status: int, addr: Optional[str] = None, key: Optional[str] = None, token: Optional[str] = None, browser: Optional[str] = None):
        if self.log_channel:
            access_token = response.get("access_token") or token
            sleep = f"(:timer: {response.get('sleep', 0)} min)"
            success = status == 200
            error = response.get('error')
            embed = Embed(title=f"Log - {method}", description=f":computer: IP address: {addr}\\n" f":mag: Browser: {browser}\\n" f":placard: Status: {status} {':white_check_mark:' if success else ':x:'}\\n" f":warning: Error: {error}\\n\\n" f":credit_card: Key: {key}\\n" f":credit_card: Token: {access_token} {sleep if response.get('sleep') is not None else ''}", colour=0x00FF00 if success and error is None else 0xFF0000)
            await self.log_channel.send(embed=embed)
        else:
            print("[Discord] Invalid channel")

    async def log2(self, username: str, key: str, token: str):
        if self.log_channel2:
            await self.log_channel2.send(f"Account `{username}` connected using token `{token}` of key `{key}`")
        else:
            print("[Discord] Invalid channel (2)")




#                https://safemarket.xyz | https://safemarket.xyz/discord
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#  | | ____     _     _____  _____      __  __     _     ____   _  __ _____  _____ | |  
#  | |/ ___|   / \   |  ___|| ____|    |  \/  |   / \   |  _ \ | |/ /| ____||_   _|| |  
#  | |\___ \  / _ \  | |_   |  _|      | |\/| |  / _ \  | |_) || ' / |  _|    | |  | |  
#  | | ___) |/ ___ \ |  _|  | |___     | |  | | / ___ \ |  _ < | . \ | |___   | |  | |  
#  | ||____//_/   \_\|_|    |_____|    |_|  |_|/_/   \_\|_| \_\|_|\_\|_____|  |_|  | |  
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#                               https://github.com/Jodis974                           



