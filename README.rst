=============================
aviio_technical_component
=============================

.. image:: https://badge.fury.io/py/aviio_technical_component.png
    :target: http://badge.fury.io/py/aviio_technical_component

.. image:: https://travis-ci.org/ckrogers/aviio_technical_component.png?branch=master
    :target: https://travis-ci.org/ckrogers/aviio_technical_component

Consumes an API endpoint (located at https://atlas.pretio.in/atlas/coding_quiz) which returns
a list of offers. The offers are ordered by the payout and saved into a csv.


============
Installation
============

At the command line either via easy_install or pip::

    $ easy_install aviio_technical_component
    $ pip install aviio_technical_component

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv aviio_technical_component
    $ pip install aviio_technical_component

========
Usage
========

You will require the API authorization token to consume the endpoint. This can be requested from
Christine K. Rogers <rogersckw@gmail.com>. This should be set to an environment variable::

    export TOKEN=xxxxx

or in Windows::

    set TOKEN=xxxxx

To use aviio_technical_component in a project::

	import aviio_technical_component

========
Feedback
========

If you have any suggestions or questions about **aviio_technical_component** feel free to email me
at rogersckw@gmail.com.

If you encounter any errors or problems with **aviio_technical_component**, please let me know!
Open an Issue at the GitHub http://github.com/ckrogers/aviio_technical_component main repository.

