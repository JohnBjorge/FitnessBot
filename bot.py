import discord
from discord.ext import commands
import asyncpg


class BirdswagBot(commands.Bot):

    def __init__(self, **options):
        self.db = None

        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="$",
            help_command=None,
            description="This is the Birdswag Bot",
            intents=intents,
            **options
        )

    async def create_db_pool(self, database, user, password, local_flag):
        if local_flag:
            self.db = await asyncpg.create_pool(database=database, user=user, password=password, host="127.0.0.1")
        else:
            self.db = await asyncpg.create_pool(database=database, user=user, password=password)