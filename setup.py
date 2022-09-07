import setuptools
from naitoon import __version__

setuptools.setup(
    name="naitoon",
    version=__version__,
    license="MIT",
    author="VoidAsMad",
    author_email="voidasmad@gmail.com",
    description="네이버 웹툰 크롤링 라이브러리",
    long_description=open("README.md", "rt", encoding="UTF8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VoidAsMad/Naitoon",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
