from os import getenv
from pprint import pprint

import giphy_client
from giphy_client.rest import ApiException

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = getenv("GIPHY_API_KEY", None)
q = "bug"  # str | Search query term or prhase.
limit = 100  # int | The maximum number of records to return. (optional) (default to 25)
offset = 0  # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = "g"  # str | Filters results by specified rating. (optional)
lang = "en"  # str | Specify default country for regional content
fmt = "json"  # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

if api_key is None:
    raise Exception("can't find GIPHY_API_KEY on environment variables")


def test_search():
    try:
        api_response = api_instance.gifs_search_get(
            api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt
        )
        # api_response.data[0].url
        print(len(api_response.data))
        assert len(api_response.data) > 0
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


def test_populate_list():
    gif_list = []
    for pg in range(0, 5):
        api_response = api_instance.gifs_search_get(
            api_key, q, limit=50, offset=pg * 10, rating=rating, lang=lang, fmt=fmt
        )
        for gif in api_response.data:
            gif_list.append(gif.images.preview_gif.url)  # api_response.data[0].images.preview_gif.url
    print(len(gif_list))
    assert len(gif_list) > 0


def test_random_gif():
    gif = api_instance.gifs_random_get(api_key, rating="g", tag="software")
    print(gif.data.url)
    assert gif
