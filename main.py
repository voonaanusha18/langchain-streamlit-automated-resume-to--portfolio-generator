import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import zipfile

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("Gemini")

st.set_page_config(page_title="AI Website Creation", page_icon="😀")
st.title("AI Automation Website Creation")

prompt = st.text_area("Write here about your website")

if st.button("Generate"):

    # Create message list
    message = [
        ("system", """
You are a highly experienced frontend web developer.

Based on the user's description, generate clean, responsive, and well-structured
HTML, CSS, and JavaScript code for a complete website.

Follow best practices in frontend development, ensure proper formatting,
and keep the code simple, readable, and modular.

Return the output strictly in the following format only:

--html--
[HTML code]
--html--

--css--
[CSS code]
--css--

--js--
[JavaScript code]
--js--
""")
       
    ]

    message.append(("user", prompt))

    # Correct model name
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    response = model.invoke(message)

    # Extract content sections safely
    html_code = response.content.split("--html--")[1]
    css_code = response.content.split("--css--")[1]
    js_code = response.content.split("--js--")[1]
    # Save files
    with open("index.html", "w") as f:
        f.write(html_code)

    with open("style.css", "w") as f:
        f.write(css_code)

    with open("script.js", "w") as f:
        f.write(js_code)

    # Create ZIP
    with zipfile.ZipFile("website.zip", "w") as zipf:
        zipf.write("index.html")
        zipf.write("style.css")
        zipf.write("script.js")

    # Download button
    st.download_button(
        "Click to download your website",
        data=open("website.zip", "rb"),
        file_name="website.zip"
    )

    st.success("Website generated successfully!")








                   
