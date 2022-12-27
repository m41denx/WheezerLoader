from setuptools import setup

setup(
    name='wheezeloader',
    version='0.2.0',
    description='Mom look I can build stuff',
    url='https://github.com/cradio/WheezerLoader',
    author='M41den',
    author_email='no-no-no',
    license='IDK',
    packages=[
        'wheezeloader',
        'wheezeloader.deezloader',
        'wheezeloader.libutils',
        'wheezeloader.models',
        'wheezeloader.spotloader'
    ],
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
