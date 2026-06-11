from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        documents
    )

    for chunk in chunks:

        text = chunk.page_content.lower()

        # --------------------------------
        # RECORDS FIRST
        # --------------------------------

        if any(
            keyword in text
            for keyword in [
                "records & milestones",
                "highest individual score",
                "highest team score",
                "most runs — career",
                "most wickets — career",
                "most centuries",
                "fastest fifty",
                "most titles",
                "highest partnership",
                "most matches — player"
            ]
        ):

            chunk.metadata["category"] = "records"

        # --------------------------------
        # BATTING
        # --------------------------------

        elif any(
            keyword in text
            for keyword in [
                "batting",
                "strike rate",
                "top batters",
                "runs scored",
                "opener",
                "century",
                "half-century"
            ]
        ):

            chunk.metadata["category"] = "batting"

        # --------------------------------
        # BOWLING
        # --------------------------------

        elif any(
            keyword in text
            for keyword in [
                "bowling",
                "economy",
                "wickets",
                "top wicket-takers",
                "best bowling",
                "fast bowling",
                "leg-spin",
                "mystery spin"
            ]
        ):

            chunk.metadata["category"] = "bowling"

        # --------------------------------
        # VENUE
        # --------------------------------

        elif any(
            keyword in text
            for keyword in [
                "venue",
                "pitch",
                "stadium",
                "batting-friendly",
                "chasing",
                "dew factor"
            ]
        ):

            chunk.metadata["category"] = "venue"

        # --------------------------------
        # GENERAL
        # --------------------------------

        else:

            chunk.metadata["category"] = "general"

    return chunks