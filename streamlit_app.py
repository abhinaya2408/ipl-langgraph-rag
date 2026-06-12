import streamlit as st
import time

from app.react.graph import react_graph

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    ToolMessage
)
# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="IPL Intelligence Assistant",
    page_icon="🏏",
    layout="wide"
)

# ----------------------------------
# Session State
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "sample_prompt" not in st.session_state:
    st.session_state.sample_prompt = None

# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.title("🏏 IPL Assistant")

    st.markdown("---")

    st.subheader("Tech Stack")

    st.write("⚡ LangGraph")
    st.write("🤖 Groq")
    st.write("📚 ChromaDB")
    st.write("🎨 Streamlit")

    st.markdown("---")

    st.subheader("System Metrics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Architecture",
            "ReAct"
        )

    with col2:
        st.metric("Tools", "4")

    st.metric(
        "Model",
        "Llama 3.1 8B"
    )

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ ReAct Agent")
    st.write("✅ Tool Calling")
    st.write("✅ LangGraph")
    st.write("✅ ChromaDB")
    st.write("✅ Metadata Retrieval")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ----------------------------------
# Header
# ----------------------------------

st.title("🏏 IPL Intelligence Assistant")

st.caption(
    "Multi-Agent RAG powered by LangGraph"
)

# ----------------------------------
# Sample Questions
# ----------------------------------

st.subheader("💡 Sample Questions")

c1, c2 = st.columns(2)

with c1:

    if st.button(
        "🏏 Who has scored the most runs?"
    ):
        st.session_state.sample_prompt = (
            "Who has scored the most runs in IPL history?"
        )

    if st.button(
        "🎯 Who has taken the most wickets?"
    ):
        st.session_state.sample_prompt = (
            "Who has taken the most wickets in IPL history?"
        )

    if st.button(
        "🏆 Which team has won the most titles?"
    ):
        st.session_state.sample_prompt = (
            "Which team has won the most IPL titles?"
        )

with c2:

    if st.button(
        "🏟 Tell me about Hyderabad pitch"
    ):
        st.session_state.sample_prompt = (
            "Tell me about Hyderabad pitch conditions"
        )

    if st.button(
        "🔥 Highest individual score"
    ):
        st.session_state.sample_prompt = (
            "Who holds the highest individual score in IPL?"
        )

    if st.button(
        "🚀 Highest team total"
    ):
        st.session_state.sample_prompt = (
            "What is the highest team total in IPL?"
        )

st.markdown("---")

# ----------------------------------
# Chat History
# ----------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )

# ----------------------------------
# Input Handling
# ----------------------------------

chat_input = st.chat_input(
    "Ask anything about IPL..."
)

prompt = chat_input

if st.session_state.sample_prompt:

    prompt = st.session_state.sample_prompt

    st.session_state.sample_prompt = None

# ----------------------------------
# Run Query
# ----------------------------------

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner(
            "Analyzing..."
        ):

            start_time = time.time()

            result = react_graph.invoke(
                {
                    "messages": [
                        HumanMessage(
                            content=prompt
                        )
                    ]
                }
            )

            messages = result["messages"]

            answer = messages[-1].content

            end_time = time.time()

            st.markdown(answer)

            st.caption(
                f"⏱ Response Time: {end_time - start_time:.2f}s"
            )

            # ----------------------------------
            # ReAct Workflow
            # ----------------------------------

            with st.expander(
                "🧠 ReAct Workflow",
                expanded=False
            ):

                for msg in messages:

                    # --------------------------
                    # User Message
                    # --------------------------

                    if isinstance(
                        msg,
                        HumanMessage
                    ):

                        st.success(
                            f"👤 User\n\n{msg.content}"
                        )

                    # --------------------------
                    # AI Message
                    # --------------------------

                    elif isinstance(
                        msg,
                        AIMessage
                    ):

                        # Tool Calls

                        if msg.tool_calls:

                            tool = msg.tool_calls[0]

                            st.info(
                                    f"""
🛠 Tool Selected

**Tool Name**
`{tool['name']}`

**Query**

```text
{tool['args'].get("query", "")}

"""
)

                        # Final Answer

                        elif msg.content:

                            st.success(
                                f"""
🤖 Final Answer

{msg.content}
"""
                            )

                    # --------------------------
                    # Tool Observation
                    # --------------------------

                    elif isinstance(
                        msg,
                        ToolMessage
                    ):

                        st.warning(
                            "📄 Tool Observation"
                        )

                        preview = (
                            msg.content[:300] + "..."
                            if len(msg.content) > 300
                            else msg.content
                        )

                        st.code(
                            preview,
                            language="text"
                        )
