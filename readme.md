# WebSocket Chat with OpenAI Compatible REST APIs

This AWS SAM template sets up a WebSocket API that integrates with OpenAI compatible REST APIs for chat completions. It leverages AWS Lambda to handle WebSocket connections, disconnections, and messages.
# Architecture

    WebSocket API: Created using AWS API Gateway, it supports WebSocket protocol for real-time communication.
    Lambda Functions: Handles connection, disconnection, and message events.
    API Gateway Routes: Defines $connect, $disconnect, and $default routes for WebSocket events.
    Layers: Includes a Lambda layer for external dependencies.

# Prerequisites

    AWS CLI configured with appropriate permissions
    AWS SAM CLI installed
    OpenAI API Key

# Deployment

## Clone the repository:


```bash
git clone https://github.com/drewski90/AWS-SAM-APIGateway-WebSocket-LLM-Completion.git
```

# Deploy the SAM template:

```bash
sam build
sam deploy --guided
```

### Follow the prompts and provide the necessary values for the parameters.

# Notes

This setup provides a robust solution for integrating WebSocket with OpenAI compatible REST APIs, supporting real-time chat applications.


# Testing

### The repository provides a index.html for testing the websocket
