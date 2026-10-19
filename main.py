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
        font-size: 2.5rem !important;    /* !important forces the browser to apply this size */
        line-height: 1.2 !important;
        font-weight: normal !important;  /* Ensures it stays clean and non-bolded */
        margin-top: 10px !important;
        margin-bottom: 20px !important;
        display: block !important;       /* Ensures it behaves like a headline block */
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
