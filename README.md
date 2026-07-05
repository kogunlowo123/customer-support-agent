# Customer Support Agent

[![CI](https://github.com/kogunlowo123/customer-support-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/customer-support-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Customer Service | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

AI customer support agent that handles inbound support requests, searches knowledge bases for solutions, resolves common issues autonomously, escalates complex cases, and maintains conversation context across channels.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `search_solutions` | Search knowledge base for solutions matching customer issue |
| `resolve_issue` | Apply an automated resolution to a customer issue |
| `lookup_customer` | Look up customer account details and history |
| `escalate_to_human` | Escalate to a human agent with full conversation context |
| `send_response` | Send a response to the customer on the appropriate channel |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/support/search` | Search solutions |
| `POST` | `/api/v1/support/resolve` | Resolve issue |
| `GET` | `/api/v1/support/customer/{customer_id}` | Lookup customer |
| `POST` | `/api/v1/support/escalate` | Escalate to human |
| `POST` | `/api/v1/support/respond` | Send response |

## Features

- Issue Resolution
- Knowledge Search
- Multi Channel
- Escalation
- Context Tracking

## Integrations

- Zendesk
- Intercom
- Freshdesk
- Salesforce Service
- Helpscout

## Architecture

```
customer-support-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── customer_support_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Help Desk + Knowledge Base + CRM**

---

Built as part of the Enterprise AI Agent Platform.
