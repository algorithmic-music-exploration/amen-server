from uploaders.s3 import get_url

def test_get_url():
    filename = "faux-filename"
    assert get_url(filename) == "https://s3-us-west-2-amazonaws.com/amen-data/faux-filename"
