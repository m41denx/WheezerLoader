from setuptools import setup

setup(
    name='wheezeloader',
    version='0.1.0',
    description='Mom look I can build stuff',
    url='https://github.com/cradio/WheezerLoader',
    author='M41den',
    author_email='no-no-no',
    license='IDK',
    packages=['wheezeloader'],
    install_requires=[
        'fastapi',
        'librespot',
        'mutagen',
        'pycryptodome',
        'requests',
        'spotipy',
        'tqdm',
        'uvicorn'
    ],
)
