import unittest
import pytest
from tests import build_full_app

@pytest.yield_fixture
def app():
    yield build_full_app()

@pytest.fixture
def test_cli(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app))

async def test_books(test_cli):
    resp = await test_cli.get('/books')
    assert resp.status == 200

if __name__ == '__main__':
    unittest.main()
