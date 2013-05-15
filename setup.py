from setuptools import setup

APP = ['app.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True}

setup(
    name='Cyberduck patch for ucloud storage',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    install_requires=['biplist', 'py2app']
)
