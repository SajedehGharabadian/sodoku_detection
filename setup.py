from setuptools import setup

def preinstall():
    f = open("readme.md","r")
    text = f.read()
    return text


setup(name="sodoku_detection",version="1.0.2",
      author="Sajedeh Gharabadiyan",
      description="first package for test",
      requires=[],
      author_email="gharabadiyansajedeh@gmail.com",
      packages=["sodoku_detection"],
      long_description=open("readme.md", 'r').read(),
      long_description_content_type='text/markdown'
    )
