from setuptools import setup, find_packages

setup(
    name='brawlstars',
    version='0.3.1',
    description='A wrapper, both asynchronous and not, for the Brawl Stars API made by Zihad!',
    long_description="I am bad at writing descriptions. TODO",
    url='https://github.com/umbresp/brawlstars',
    author='Umbresp',
    author_email='umbresp63@gmail.com',
    license='MIT',
    keywords=['brawlstars brawl stars'],
    packages=find_packages(),
    install_requires=['requests', 'python-box', 'aiohttp']
)
