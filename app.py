#!/usr/bin/python
# -*-coding:utf8 -*-

import random
import json
import os

from bottle import route, run, request, template
from imgurpython import ImgurClient


def get_subreddit_list(sub):
    """
    We can add as many subreddits as we want.
    """
    if sub == "food":
        return [u'FoodPorn', u'food', u'Pizza', u'Ramen']


def get_random_image(sub):
    """
    Returns 15 random images from a random subreddit based in the `sub` param.
    """
    client_id = os.environ.get('IMGUR_CLIENT_ID')
    client_secret = os.environ.get('IMGUR_CLIENT_SECRET')

    if client_id and client_secret:
        client = ImgurClient(client_id, client_secret)

        subreddit_list = get_subreddit_list(sub)
        subreddit = client.subreddit_gallery(random.choice(subreddit_list))

        # Uncomment this if you want just a single image to be returned.
        # return random.choice(subreddit).link

        # We'll return 15 imgur photo links, each in its own line.
        sample = random.sample(subreddit, 15)
        return "\n".join([item.link for item in sample])


@route('outgoing/<sub>', method=["POST", "GET"])
def outgoing(sub):
    """
        @SlackHQ's Outgoing Webhooks require a POST request which response should be a JSON obj with a 'text' field.
    """
    if request.method == "POST":
        response = {"text": get_random_image(sub)}
        return json.dumps(response)
    else:
        return template("<h1>Nothing to see here just yet!</h1>")


if __name__ == "__main__":
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, debug=True)
