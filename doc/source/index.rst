.. reg_utils documentation master file, created by
   sphinx-quickstart on Wed May 23 14:52:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

reg_utils package
=====================================

Introduction
------------
``reg_utils`` package provides a lightweight and easy to use toolkit to work with XML register address tables. 
It consists of two subpackages: ``reg_interface`` and ``reg_generator`` and a C++ library ``rwreg`` available for x86 and ARM architectures. 

* ``reg_interface`` allows to read the address tables and perform atomic operations with registers and can be extended with more complex methods. 
* ``reg_generator`` allows to generate firmware registers based on the XML address table.

Table of contents:
------------------

.. toctree::
   :maxdepth: 2

   installation
   reg_interface/usage/quickstart
   reg_interface/reg_interface

.. toctree::
   :caption: API documentation for the rwreg library
   :maxdepth: 1

   rwreg/rwreg_x86.rst
   exhale-api/api

.. toctree::
   :caption: reg_utils python API
   :maxdepth: 1

   autoapi/reg_generator/index
   autoapi/reg_interface/index
   sphinx-api-new-options/modules.rst
   sphinx-api-old-options/modules.rst

.. toctree::
   :hidden:
   :caption: Links to other documentation
   :maxdepth: 1

   CMS GEM DAQ project page <http://0.0.0.0:8000>
   Users guide <http://0.0.0.0:8000/SITE_ROOT/guides/userguide>
   Expert guide <http://0.0.0.0:8000/SITE_ROOT/guides/expertguide>
   Developer guide <http://0.0.0.0:8000/SITE_ROOT/guides/devguide>

.. toctree::
   :hidden:
   :caption: Links to API documentation
   :maxdepth: 1

   cmsgemos <http://0.0.0.0:8000/SITE_ROOT/docs/api/cmsgemos/latest>
   gemplotting <http://0.0.0.0:8000/site_root/docs/api/gemplotting/latest>
   vfatqc <http://0.0.0.0:8000/site_root/docs/api/vfatqc/latest>
   ctp7_modules <http://0.0.0.0:8000/site_root/docs/api/ctp7_modules/latest>
   reg_utils (this site) <http://0.0.0.0:8000/site_root/docs/api/reg_utils/latest>
   xhal <http://0.0.0.0:8000/site_root/docs/api/xhal/latest>
   reg_interface_gem <http://0.0.0.0:8000/SITE_ROOT/docs/api/reg_interface_gem/latest>
   reedmuller-c <http://0.0.0.0:8000/site_root/docs/api/reedmuller-c/latest>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

