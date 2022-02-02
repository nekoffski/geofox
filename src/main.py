import os
from discord.ext import commands
from cogs import cogs


def main():
    token = os.getenv("GEOFOX_TOKEN")

    if token is None:
        raise RuntimeError("GEOFOX_TOKEN venv is not specified")

    client = commands.Bot(command_prefix="*")
    client.remove_command("help")

    for cog in cogs:
        client.add_cog(cog)

    client.run(token)


if __name__ == '__main__':
    main()
