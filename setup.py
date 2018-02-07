from setuptools import setup, find_packages

setup(
    name='brawlstars',
    version='0.0.3',
    description='Nothing here yet...',
    long_description="Nothing here yet...",
    url='https://github.com/umbresp/brawlstars',
    author='Umbresp',
    author_email='umbresp63@gmail.com',
    license='MIT',
    keywords=['brawlstars brawl stars'],
    packages=find_packages(),
    install_requires=['requests', 'python-box', 'aiohttp']
)
