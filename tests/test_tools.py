from app.tools.records_tool import (
    search_records
)

result = search_records.invoke(
    {
        "query":
        "highest individual score"
    }
)

print(result)