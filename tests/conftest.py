"""Test configuration for Customer Support Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "customer-support-agent", "category": "Customer Service"}
