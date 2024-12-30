import setuptools

__version__ = "0.0.0"

REPO_NAME = "E2E-ML"
AUTHOR_USER_NAME = "110119076"
AUTHOR_EMAIL = "venkataped@gmail.com"
SRC_REPO = "iplPredictor"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="End to end ML app",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)