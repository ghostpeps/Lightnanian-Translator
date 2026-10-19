import streamlit as st

st.markdown(
    """
    <style>
    @font-face {
        font-family: 'New Font';
        src: url('app/static/slovanian.otf') format('opentype');
        font-weight: normal;
        font-style: normal;
    }
    
    .custom-font-text {
        font-family: 'New Font', sans-serif;
        font-size: 28px;
        line-height: 1.5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def write_font(text: str):
    """Outputs standalone text containers using sitelen pona."""
    st.markdown(
        f'<p class="custom-font-text">{text}</p>', 
        unsafe_allow_html=True
    )

st.title("GitHub Hosted Custom Font")
st.write("Regular default text looks like this.")

write_font("toki pona li pona")
