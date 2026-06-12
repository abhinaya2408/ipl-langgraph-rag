import streamlit as st
import time

from app.graph.builder import graph

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
        st.metric("Agents", "4")

    with col2:
        st.metric("Tools", "4")

    st.metric(
        "Model",
        "Llama 3.1 8B"
    )

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ Multi-Agent Routing")
    st.write("✅ Metadata Retrieval")
    st.write("✅ Tool Calling")
    st.write("✅ ChromaDB")
    st.write("✅ LangGraph")

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

            result = graph.invoke(
                {
                    "user_query": prompt
                }
            )

            answer = result["final_answer"]

            end_time = time.time()

            st.markdown(answer)

            st.caption(
                f"⏱ Response Time: {end_time - start_time:.2f}s"
            )

            # ----------------------------------
            # Workflow
            # ----------------------------------

            query_type = result.get(
                "query_type",
                "unknown"
            )

            tool_used = result.get(
                "tool_used",
                "No Tool"
            )
            with st.expander(
            "🔄 Agent Workflow"
            ):

                st.success(
                    "✅ Router Agent"
                )

                st.markdown("⬇️")

                st.info(
                    f"🤖 {query_type.title()} Agent"
                )

                st.markdown("⬇️")

                st.warning(
                    f"🛠 Tool Used: {tool_used}"
                )

                st.markdown("⬇️")

                st.success(
                    "✅ Synthesis Agent"
                )

            # ----------------------------------
# Tool Information
# ----------------------------------

            with st.expander(
                "🛠 Tool Information"
            ):

                st.write(
                    f"Selected Tool: `{tool_used}`"
                )

            # ----------------------------------
            # Sources
            # ----------------------------------

            sources = result.get(
                "sources",
                []
            )

            with st.expander(
                "📚 Retrieved Sources"
            ):

                if not sources:

                    st.info(
                        "No source chunks available."
                    )

                else:

                    for idx, source in enumerate(
                        sources,
                        start=1
                    ):

                        st.markdown(
                            f"### Source {idx}"
                        )

                        st.write(source)

                        st.divider()

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )