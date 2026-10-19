import streamlit as st

st.markdown(
    """
    <style>
    @font-face {
        font-family: 'New Font';
        src: url('app/libraries/slovanian.otf') format('opentype');
        font-weight: normal;
        font-style: normal;
    }
    
    .custom-font-text {
        font-family: 'New Font', sans-serif !important;
        font-size: 5.0rem !important;
        line-height: 1.1 !important;
        font-weight: normal !important;  
        margin-top: 15px !important;
        margin-bottom: 25px !important;
        display: block !important;       
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

st.title("Lightnanian Translator")


write_font("random")
