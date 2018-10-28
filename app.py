import importlib
import sys
import aiohttp
import asyncio


def import_source(s_name):
    dot_index = s_name.rfind('.')
    class_name = s_name[dot_index+1:]
    source_module = importlib.import_module('sources.'+s_name[:dot_index])
    return getattr(source_module, class_name)


async def main(sources, configs):
    source_classes = []
    for s_name in sources:
        source_classes.append(import_source(s_name))

    async with aiohttp.ClientSession() as session:
        for idx, s in enumerate(source_classes):
            si = s(session, **configs[idx])
            await si.fetch()
            await si.render()


if __name__ == '__main__':
    sources = ['httpcodesource.HttpCodeSource',
               'httpcodesource.HttpCodeSource']
    configs = [{'url': 'http://python.org'}, {'url': 'http://google.com'}]
    asyncio.run(main(sources, configs))
