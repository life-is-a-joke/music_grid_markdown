from setuptools import setup

setup(
    name='musicmd',
    version='0.4.0',
    url='https://github.com/yathit/music_grid_markdown',
    entry_points={
        'mkdocs.plugins': [
            'musicgrid = musicgrid.musicgrid:MusicGridPlugin',
        ]
    }
)
