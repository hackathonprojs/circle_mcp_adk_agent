# Circle MCP ADK Agent

This is a Python-based agent implementation using MCP (Multi-Cloud Platform) (in our github directory) and google ADK.

## Prerequisites

- google-adk

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd circle_mcp_adk_agent
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies (this includes google-adk):
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
source setenv.sh
```

## Running the Application

To run the application, use:
```bash
adk web
```
or

```bash
adk web --host 0.0.0.0 --port 5050
```


## Project Structure

- `multi_tool_agent/`: Main application code
- `requirements.txt`: Python dependencies
- `setenv.sh`: Environment variable configuration
- `deploy.sh`: Deployment script
- `logs/`: Application logs directory

## Features

- MCP ADK integration


## Development

For development purposes, make sure to:
1. Keep your virtual environment activated
2. Use the provided environment variables


## License

[Add your license information here]

## Contributing

[Add contribution guidelines if applicable]
