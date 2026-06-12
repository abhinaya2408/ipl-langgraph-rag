from app.tools.batting_tool import (
    search_batting_stats
)

from app.tools.bowling_tool import (
    search_bowling_stats
)

from app.tools.venue_tool import (
    search_venue_info
)

from app.tools.records_tool import (
    search_records
)


TOOLS = [

    search_batting_stats,

    search_bowling_stats,

    search_venue_info,

    search_records

]