.. _contributing:

Contributing
==========================

Python developper setup
--------------------------

It is not necessary to build the Javascript bundle when developping the python side of HiPlot. However, the generated bundle (:code:`hiplot/static/built/hiplot.bundle.js`) is not
provided in the git repository. The easiest solution is to download the latest version generated by the CI: :download:`hiplot.bundle.js <../hiplot/static/built/hiplot.bundle.js>`

Building Javascript bundle
--------------------------

HiPlot's frontend is built with React in TypeScript. Those files need to be compiled and bundled into plain Javascript to generate :code:`hiplot.bundle.js`.

* Node/npm is required in order to build those files
* Required packages can be installed with :code:`npm install` from HiPlot root directory
* To build files :code:`npm run build` (or in development mode :code:`npm run build-dev`)



Building documentation
--------------------------

.. code-block:: bash

    pip install -r requirements/dev.txt
    cd docs
    make html
