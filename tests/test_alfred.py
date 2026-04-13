from nightwing.alfred.server import create_server


def test_create_server_ready():
    result = create_server()
    assert result["status"] == "ready"
