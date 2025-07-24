import streamlit as st
from app.graph import build_graph

st.title("AI Article Generator")

topic = st.text_input("Enter a topic for your article:")

if st.button("Generate Article") and topic:
    app = build_graph()
    state = {
        "topic": topic,
        "critic_count": 0,
        "draft": "",
        "feedback": "",
        "good_enough": False,
        "final_article": ""
    }
    with st.spinner("Generating article..."):
        result = app.invoke(state)
        print(result)  # Debugging line to check the result structure
    st.subheader("Generated Article")
    st.markdown(result["final_article"])