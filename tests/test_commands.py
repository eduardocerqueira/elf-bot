import json
from slack_sdk import WebClient

from typing import Callable

from slack_bolt import App, Ack, BoltResponse, Say
from mock_web_api_server import (
    setup_mock_web_api_server,
    cleanup_mock_web_api_server,
)
from utils import remove_os_env_temporarily, restore_os_env


class NoopAck(Ack):
    def __call__(self) -> BoltResponse:
        pass


class TestCommands:
    signing_secret = "secret"
    valid_token = "xoxb-valid"
    mock_api_server_base_url = "http://localhost:8888"
    channel = "C111"
    ack = NoopAck()
    web_client = WebClient(
        token=valid_token,
        base_url=mock_api_server_base_url)

    def setup_method(self):
        self.old_os_env = remove_os_env_temporarily()
        setup_mock_web_api_server(self)

    def teardown_method(self):
        cleanup_mock_web_api_server(self)
        restore_os_env(self.old_os_env)

    def test_mock_server_is_running(self):
        resp = self.web_client.api_test()
        assert resp != None

    def test_test_elf(self):
        app = App(
            signing_secret=self.signing_secret,
            client=self.web_client)

        @app.command("/test")
        def handle_commands(ack: Ack, body: dict):
            assert body is not None
            ack()

        handle_commands(self.ack, {})
        assert isinstance(handle_commands, Callable)

    def test_test_day(self):
        app = App(
            signing_secret=self.signing_secret,
            client=self.web_client)

        @app.command("/testday")
        def handle_commands(ack: Ack, body: dict):
            assert body is not None
            ack()

            with open('elf/data/testday.json') as f:
                data = json.load(f)

            if "blocks" not in data or len(data["blocks"]) == 0:
                print("I couldn't find any testday scheduled yet")
                return

            # TODO: hide or mark old events with icon, need think more about it

            for event in data["blocks"]:
                print(event)

        handle_commands(self.ack, {})
        assert isinstance(handle_commands, Callable)
