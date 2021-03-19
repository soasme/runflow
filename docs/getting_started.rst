.. _Getting Started:

Getting Started
===============

In this quick start guide, we will bootstrap a Jetflow instance on your local machine.

Install Jetflow
---------------

Install Jetflow using `pip`:

.. code-block:: console

    $ mkdir app
    $ cd app
    $ python3 -mvenv venv
    $ source venv/bin/activate
    $ python3 -mpip install jetflow

Run Jetflow
-----------

Run Jetflow using `jetflow`:

.. code-block:: console

    $ jetflow worker
    Jetflow has no scheduled jobs currently.
    Jetflow is listening on http://0.0.0.0:8964

Now, you should be able to browse the Jetflow GUI from your browser:
`http://localhost:8964 <http://localhost:8964>`_.

What's Next?
------------

From this point, you can head to :ref:`Tutorials` for further examples and
:ref:`How-To` for solving a real-world problem.
