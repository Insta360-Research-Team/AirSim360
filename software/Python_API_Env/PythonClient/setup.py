import re
import pathlib

import setuptools

HERE = pathlib.Path(__file__).resolve().parent
INIT_FILE = HERE / "airsim" / "__init__.py"

_version_match = re.search(
    r'^__version__\s*=\s*["\']([^"\']+)["\']',
    INIT_FILE.read_text(encoding="utf-8"),
    re.MULTILINE,
)
if _version_match is None:
    raise RuntimeError(
        f"Cannot locate __version__ in {INIT_FILE}; expected `__version__ = \"x.y.z\"`."
    )
__version__ = _version_match.group(1)

readme_path = HERE / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setuptools.setup(
    name="airsim",
    version=__version__,
    author="Shital Shah",
    author_email="shitals@microsoft.com",
    description="Open source simulator based on Unreal Engine for autonomous vehicles from Microsoft AI & Research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microsoft/airsim",
    packages=["airsim"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "msgpack-rpc-python",
        "opencv-python",
        "matplotlib",
    ],
)
