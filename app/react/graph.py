from langgraph.checkpoint.memory import MemorySaver

from app.react.builder import builder

# ---------------------------------------
# Memory Checkpointer
# ---------------------------------------

memory = MemorySaver()

# ---------------------------------------
# Compile Graph
# ---------------------------------------

react_graph = builder.compile(
    checkpointer=memory
)