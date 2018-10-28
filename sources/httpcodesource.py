import aiohttp
import asyncio
import time
from sources.source import Source


class HttpCodeSource(Source):
    """HttpCodeSource allows you to fetch a page and render the status code

    This is a simple Source that does only one thing: it fetches a web
    page provided from a URL, and renders the URL with the corresponding
    HTTP status code.
    """
    def __init__(self, aio_session, url):
        super(HttpCodeSource, self).__init__(aio_session)
        self.url = url

    async def fetch(self):
        async with self.session.get(self.url) as response:
            self.content = response.status

    async def render(self):
        print('{}: {}'.format(self.url, self.content))
