from setuptools import setup

setup(
    name="soksaccounts",
    version="1.1.0",
    author="chenjiandongx",
    author_email="chenjiandongx@qq.com",
    url="https://github.com/chenjiandongx/soksaccouts",
    description=" Generate shadowsocks gui-config.json automatically",
    license="MIT",
    py_modules=["soks"],
    entry_points={"console_scripts": ["soks=soks:main"]},
)
