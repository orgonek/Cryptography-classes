from setuptools import setup, find_packages

setup(
    name='fastAPI_crypto',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click~=7.1.2',
        'cryptography~=3.4.7',
        'fastapi~=0.63.0',
        'pydantic~=1.8.1',
        'uvicorn~=0.12.3',
        'aiofiles~=0.6.0',
        'Jinja2~=2.11.3',
        'python-multipart~=0.0.5'
    ],
)
