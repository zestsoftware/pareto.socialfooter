from setuptools import setup, find_packages

version = '1.4.dev0'

setup(name='pareto.socialfooter',
      version=version,
      description="Footer viewlet with social buttons",
      long_description=(open("README.rst").read() + "\n" +
                        open("CHANGES.rst").read()),
      # Get more strings from
      # https://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          ],
      keywords='social buttons',
      author='Pareto and Zest',
      author_email='info@zestsoftware.nl',
      url='https://github.com/zestsoftware/pareto.socialfooter',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pareto'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
