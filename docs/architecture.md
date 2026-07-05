# Customer Support Agent Architecture

AI customer support agent that handles inbound support requests, searches knowledge bases for solutions, resolves common issues autonomously, escalates complex cases, and maintains conversation context across channels.

## Domain Tools

- **search_solutions**: Search knowledge base for solutions matching customer issue
- **resolve_issue**: Apply an automated resolution to a customer issue
- **lookup_customer**: Look up customer account details and history
- **escalate_to_human**: Escalate to a human agent with full conversation context
- **send_response**: Send a response to the customer on the appropriate channel