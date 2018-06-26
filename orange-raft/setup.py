from setuptools import setup

setup(name="Raft",
      version='0.1',
      packages=["raft"],
      package_data={"raft": ["icons/*.svg", "icons/*.JPG"]},
      classifiers=["Example :: Invalid"],
      # Declare orangedemo package to contain widgets for the "Demo" category
      entry_points={"orange.widgets": "Valdir = raft"},
      )
