from mcp.types import Tool

SEARCH_PAPERS_SCHEMA = Tool(
    name="search_papers",
    description="Search for academic papers based on a query",
    inputSchema={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query for papers"
            },
            "max_results": {
                "type": "integer",
                "description": "Maximum number of results to return",
                "default": 10
            }
        },
        "required": ["query"]
    }
)

EXTRACT_INFO_SCHEMA = Tool(
    name="extract_info",
    description="Extract specific information from a paper",
    inputSchema={
        "type": "object",
        "properties": {
            "paper_id": {
                "type": "string",
                "description": "ID of the paper to extract info from"
            },
            "info_type": {
                "type": "string",
                "description": "Type of information to extract"
            }
        },
        "required": ["paper_id", "info_type"]
    }
)