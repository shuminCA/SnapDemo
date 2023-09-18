import os
from typing import Any
from dotenv import load_dotenv
from embedchain import App

load_dotenv()

wikipedia_bot = App()
# # Embed Online Resources
# wikipedia_bot.add("https://en.wikipedia.org/wiki/Donald_Trump")
# wikipedia_bot.add("https://en.wikipedia.org/wiki/Barack_Obama")

def run_llm(query: str) -> Any:
    if wikipedia_bot is None:
        return "Please add a Wiki Link first!"
    return wikipedia_bot.query(query)

def add_url(url: str):
    wikipedia_bot.add(url)
