# streamming

#we need to use graph.stream in place of invoke that we return generator
# Refer Page https://docs.langchain.com/oss/python/langgraph/streaming
for chunk in graph.stream(
    {"topic": "ice cream"},
    stream_mode="messages",
    version="v2",
):
    if chunk["type"] == "messages":
        message_chunk, metadata = chunk["data"]
        if message_chunk.content:
            print(message_chunk.content, end="|", flush=True)




# For Streamlit UI
# https://docs.streamlit.io/develop/api-reference/chat