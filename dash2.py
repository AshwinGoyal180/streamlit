import streamlit as st

def apply_dynamic_theme():
    """Simple CSS-only dynamic theme that responds to browser preference"""
    theme_css = """
    <style>
    /* Variables for light mode (default) */
    :root {
        --primary-bg: #ffffff;
        --secondary-bg: #f0f2f6;
        --text-color: #262730;
        --accent-color: #F39C12;
        --border-color: #e0e0e0;
        --sidebar-bg: #f8f9fa;
    }

    /* Dark mode - automatically applied when browser is in dark mode */
    @media (prefers-color-scheme: dark) {
        :root {
            --primary-bg: #14131f;
            --secondary-bg: #1e1d2e;
            --text-color: #ffffff;
            --accent-color: #F39C12;
            --border-color: #333333;
            --sidebar-bg: #262730;
        }
    }

    /* Apply theme to Streamlit elements */
    .stApp {
        background-color: var(--primary-bg) !important;
        color: var(--text-color) !important;
    }

    .stApp > header {
        background-color: transparent !important;
    }

    .stApp > div:first-child {
        background-color: var(--primary-bg) !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: var(--sidebar-bg) !important;
    }

    section[data-testid="stSidebar"] > div {
        background-color: var(--sidebar-bg) !important;
    }

    /* Input elements */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: var(--secondary-bg) !important;
        color: var(--text-color) !important;
        border-color: var(--border-color) !important;
    }

    .stSelectbox > div > div {
        background-color: var(--secondary-bg) !important;
        color: var(--text-color) !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: var(--accent-color) !important;
        color: white !important;
        border: none !important;
        border-radius: 5px !important;
    }

    .stButton > button:hover {
        opacity: 0.8 !important;
    }

    /* Metrics */
    div[data-testid="metric-container"] {
        background-color: var(--secondary-bg) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
    }

    /* Dataframes */
    .stDataFrame {
        background-color: var(--secondary-bg) !important;
    }

    /* Markdown */
    .stMarkdown {
        color: var(--text-color) !important;
    }

    /* Success/Error/Warning messages */
    .stAlert {
        background-color: var(--secondary-bg) !important;
        border-color: var(--border-color) !important;
        color: var(--text-color) !important;
    }

    /* Charts background */
    .js-plotly-plot, .plotly {
        background-color: var(--primary-bg) !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: var(--secondary-bg) !important;
    }

    .stTabs [data-baseweb="tab"] {
        color: var(--text-color) !important;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: var(--secondary-bg) !important;
        color: var(--text-color) !important;
    }
    </style>
    """
    st.markdown(theme_css, unsafe_allow_html=True)

def add_manual_theme_toggle():
    """Optional: Add manual theme override without JavaScript"""
    if 'manual_theme' not in st.session_state:
        st.session_state.manual_theme = 'auto'

    # Theme selector in sidebar
    with st.sidebar:
        theme_choice = st.radio(
            "🎨 Theme",
            ['auto', 'light', 'dark'],
            index=['auto', 'light', 'dark'].index(st.session_state.manual_theme),
            help="Auto follows your browser/system preference"
        )
        st.session_state.manual_theme = theme_choice

    # Apply manual override if needed
    if theme_choice == 'light':
        st.markdown("""
        <style>
        :root {
            --primary-bg: #ffffff !important;
            --secondary-bg: #f0f2f6 !important;
            --text-color: #262730 !important;
            --sidebar-bg: #f8f9fa !important;
        }
        </style>
        """, unsafe_allow_html=True)
    elif theme_choice == 'dark':
        st.markdown("""
        <style>
        :root {
            --primary-bg: #14131f !important;
            --secondary-bg: #1e1d2e !important;
            --text-color: #ffffff !important;
            --sidebar-bg: #262730 !important;
        }
        </style>
        """, unsafe_allow_html=True)

# Demo app
def main():
    st.set_page_config(
        page_title="Dynamic Theme Demo",
        page_icon="🌙",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Apply the dynamic theme (this is the key part!)
    apply_dynamic_theme()

    # Optional manual toggle
    add_manual_theme_toggle()

    # Your app content
    st.title("🌙 Dynamic Theme Demo")
    st.write("This automatically switches between light and dark based on your browser/system settings!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Users", "1,234", "+12%")
    with col2:
        st.metric("Revenue", "$45K", "+8%")
    with col3:
        st.metric("Growth", "23%", "+5%")

    st.subheader("Test Elements")

    name = st.text_input("Enter your name", placeholder="John Doe")
    option = st.selectbox("Choose option", ["Option 1", "Option 2", "Option 3"])

    if st.button("Test Button"):
        st.success(f"Hello {name}! You selected {option}")
        st.info("This is an info message")
        st.warning("This is a warning")
        st.error("This is an error message")

    # Test expander
    with st.expander("Click to expand"):
        st.write("This content is inside an expander!")

    # Test tabs
    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
    with tab1:
        st.write("Content in tab 1")
    with tab2:
        st.write("Content in tab 2")

    st.markdown("---")
    st.markdown("""
    ### How to use in your app:

    1. Copy the `apply_dynamic_theme()` function
    2. Call it at the start of your app (after `st.set_page_config`)
    3. That's it! No JavaScript, no blank screens.

    **The theme will automatically switch when you:**
    - Change your system theme (Windows/Mac/Linux)
    - Change browser theme preference
    - Use browser dev tools to toggle dark mode
    """)

if __name__ == "__main__":
    main()
