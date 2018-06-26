from setuptools import setup

setup(name="Lunchtime",
      version='0.1',
      packages=["lunchtime"],
      package_data={"lunchtime": ["icons/*.svg"]},
      classifiers=["Example :: Invalid"],
      # Declare orangedemo package to contain widgets for the "Demo" category
      entry_points={"orange.widgets": "Valdir = lunchtime"},
      )
