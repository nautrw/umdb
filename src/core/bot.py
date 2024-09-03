import os
import platform
import sys

import disnake
from disnake.ext import commands

from src.core.config import CONFIG as config


class Bot(commands.InteractionBot):
    def __init__(self):
        self.config = config

        super().__init__(test_guilds=self.config["test_guilds"])

    def load_extensions(self, exts_list):
        loaded_exts_count = 0

        for ext in exts_list:
            try:
                self.load_extension(ext)
                print(f"Loaded extension: {ext}")
                loaded_exts_count += 1
            except Exception as exception:
                print(f"{type(exception).__name__}: {exception}")

            print(
                f'{loaded_exts_count} extension{"s" if loaded_exts_count != 1 else ""} loaded'
            )

    async def on_connect(self):
        print(f"Connected to {len(self.guilds)} guilds")
        print(f"Using Disnake version {disnake.__version__}")
        print(f"Using Python version {sys.version}")
        print(f"Using platform {platform.system()} {platform.release()} {os.name}")
        print(f"Successfully logged in as {self.user} (ID: {self.user.id})")

    def main(self):
        self.load_extensions(self.config["exts"])
        self.run(config["token"])
