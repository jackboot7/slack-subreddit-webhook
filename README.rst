Send subreddit's photos to a Slack Channel
==========================================

This small `bottle.py` application implements a Slack Outgoing Webhook to send a group (default 15) of photos to a SlackHQ_ channel.

To use it, you'll need to have the Imgur API's credentials, which can be obtained at `Imgur's API page`_.

You'll have to add a Outgoing-Webhook to your Slack app, using your configured URL.

In case you want to push data into `private groups` or `DMs`, you'll have to configure an Incoming Webhook and Slack Command.

Installation
============

Local
-----

.. code:: bash

   $ pip install imgurpython
   $ pip install bottle

Or

.. code:: bash

   $ pip install -r requirements.txt


Then add some enviroment variables

.. code:: bash

    $ export IMGUR_CLIENT_ID=<your Imgur client id>
    $ export IMGUR_CLIENT_SECRET=<your Imgur client secret>


Heroku
------

After following the Heroku documentation to push your code, you must add three ENV variables:

.. code:: bash

    $ heroku config:set APP_LOCATION=heroku
    $ heroku config:set IMGUR_CLIENT_ID=<your Imgur client id>
    $ heroku config:set IMGUR_CLIENT_SECRET=<your Imgur client secret>

If you're using Incoming Webhooks with the `incoming` function, you must add:

.. code:: bash

    $ heroku config:set SLACK_CHANNEL=<your channel/private group/dm>



.. _SlackHQ: https://slack.com/
.. _Imgur's API page: https://api.imgur.com/ 
