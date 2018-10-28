import sys
import importlib
import aiohttp
import asyncio


def import_source(s_name):
    dot_index = s_name.rfind('.')
    class_name = s_name[dot_index+1:]
    source_module = importlib.import_module('sources.'+s_name[:dot_index])
    return getattr(source_module, class_name)


async def main(sources):
    async with aiohttp.ClientSession() as session:
        for source in sources:
            source_class = import_source(source['name'])
            source_instance = source_class(session, **source['config'])
            await source_instance.fetch()
            await source_instance.render()


if __name__ == '__main__':
    try:
        from config import SOURCES
    except ImportError:
        print('Configuration file config.py is missing.')
        print('Copy from config.py.example to use as a base config file.')
        sys.exit(1)
    except SyntaxError:
        print('Syntax error in config.py')
        sys.exit(1)

    asyncio.run(main(SOURCES))
