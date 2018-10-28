import aiohttp


class Source(object):
    """Source is a data source capable of fetching and rendering data.

    To create your own custom data source, you should subclass this class
    and override it with your own fetch() and render() functions.

    aiohttp is provided to all Source classes to fetch data over HTTP.

    See httpcodesource.py for an example on how to build your own simple
    data Source class.
    """

    def __init__(self, aio_session):
        self.session = aio_session

    async def fetch(self, *args, **kwargs):
        pass

    async def render(self, *args, **kwargs):
        pass
