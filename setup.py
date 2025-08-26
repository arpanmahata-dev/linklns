import setuptools

with open("README.md","r",encoding="utf-8") as fh:
    long_description = f.read()

__version__ = "0.1.0"
REPO_NAME = "linklns"
SRC_REPO = "linklns"
AUTHOR_USER_NAME = "arpanmahata-dev"
AUTHOR_EMAIL = "arpanmahato09@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description="A Python tool to link media into Notebook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)