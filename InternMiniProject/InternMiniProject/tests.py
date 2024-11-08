from InternMiniProject.utils.json_processor import JsonProcessor


def test_json_flatten():
    json = {"slack_proxy_message": "hello"}
    json_processor = JsonProcessor()
    json_processor.flatten(json)
    assert json_processor.data[".slack_proxy_message"] == "hello"


def test_get_json():
    json = {"slack_proxy_message": "hello"}
    json_processor = JsonProcessor()
    json_processor.flatten(json)
    assert json == json_processor.get_json()
