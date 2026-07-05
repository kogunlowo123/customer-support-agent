"""Customer Support Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_search_solutions():
    """Test Search knowledge base for solutions matching customer issue."""
    tools = AgentTools()
    result = await tools.search_solutions(issue_description="test", product="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_resolve_issue():
    """Test Apply an automated resolution to a customer issue."""
    tools = AgentTools()
    result = await tools.resolve_issue(ticket_id="test", resolution_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_lookup_customer():
    """Test Look up customer account details and history."""
    tools = AgentTools()
    result = await tools.lookup_customer(customer_id="test", include_history=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_escalate_to_human():
    """Test Escalate to a human agent with full conversation context."""
    tools = AgentTools()
    result = await tools.escalate_to_human(ticket_id="test", reason="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.customer_support_agent_agent import CustomerSupportAgentAgent
    agent = CustomerSupportAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
