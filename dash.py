# # # # # import streamlit as st
# # # # # import pandas as pd
# # # # # import ydata_profiling
# # # # # from streamlit_pandas_profiling import st_profile_report
# # # # #
# # # # # st.header('`streamlit_pandas_profiling`')
# # # # #
# # # # # # df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
# # # # # #
# # # # # # pr = df.profile_report()
# # # # # # st_profile_report(pr)
# # # # #
# # # # # st.button('hello')
# # # #
# # # #
# # # # # import streamlit as st
# # # # #
# # # # # st.title('Customizing the theme of Streamlit apps')
# # # # #
# # # # # st.write('Contents of the `.streamlit/config.toml` file of this app')
# # # # #
# # # # # st.code("""
# # # # # [theme]
# # # # # primaryColor="#F39C12"
# # # # # backgroundColor="#2E86C1"
# # # # # secondaryBackgroundColor="#AED6F1"
# # # # # textColor="#FFFFFF"
# # # # # font="monospace"
# # # # # """)
# # # # #
# # # # # number = st.sidebar.slider('Select a number:', 0, 10, 5)
# # # # # st.write('Selected number from slider widget is:', number)
# # # # #
# # # # #
# # # # # st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
# # # #
# # # #
# # # #
# # # # # Import python packages
# # # # import streamlit as st
# # # # import pandas as pd
# # # # # from snowflake.snowpark.context import get_active_session
# # # #
# # # # # Write directly to the app
# # # # st.title(f"Example Streamlit App :balloon: {st.__version__}")
# # # # st.write(
# # # #   """Replace this example with your own code!
# # # #   **And if you're new to Streamlit,** check
# # # #   out our easy-to-follow guides at
# # # #   [docs.streamlit.io](https://docs.streamlit.io).
# # # #   """
# # # # )
# # # #
# # # # # Get the current credentials
# # # # # session = get_active_session()
# # # #
# # # # # Use an interactive slider to get user input
# # # # hifives_val = st.slider(
# # # #   "Number of high-fives in Q3",
# # # #   min_value=0,
# # # #   max_value=90,
# # # #   value=60,
# # # #   help="Use this to enter the number of high-fives you gave in Q3",
# # # # )
# # # #
# # # # # #  Create an example dataframe
# # # # # #  Note: this is just some dummy data, but you can easily connect to your Snowflake data
# # # # # #  It is also possible to query data using raw SQL using session.sql() e.g. session.sql("select * from table")
# # # # # created_dataframe = session.create_dataframe(
# # # # #   [[50, 25, "Q1"], [20, 35, "Q2"], [hifives_val, 30, "Q3"]],
# # # # #   schema=["HIGH_FIVES", "FIST_BUMPS", "QUARTER"],
# # # # # )
# # # #
# # # # # Execute the query and convert it into a Pandas dataframe
# # # # queried_data = pd.DataFrame(
# # # #     [[50, 25, "Q1"], [20, 35, "Q2"], [hifives_val, 30, "Q3"]],
# # # #     columns=["HIGH_FIVES", "FIST_BUMPS", "QUARTER"]
# # # # )
# # # #
# # # # # Create a simple bar chart
# # # # # See docs.streamlit.io for more types of charts
# # # # st.subheader("Number of high-fives")
# # # # st.bar_chart(data=queried_data, x="QUARTER", y="HIGH_FIVES")
# # # #
# # # # st.subheader("Underlying data point")
# # # # st.dataframe(queried_data, use_container_width=True)
# # #
# # #
# # #
# # # # Method 1: Simple CSS-only approach
# # # def simple_auto_theme():
# # #     """Minimal CSS-only auto theme"""
# # #     st.markdown("""
# # #     <style>
# # #     /* Auto-adapting theme */
# # #     .stApp {
# # #         background-color: light-dark(#ffffff, #0e1117);
# # #         color: light-dark(#262730, #fafafa);
# # #     }
# # #
# # #     .stSidebar {
# # #         background-color: light-dark(#f0f2f6, #262730);
# # #     }
# # #
# # #     /* Modern CSS light-dark() function - newer browsers only */
# # #     .stButton > button {
# # #         background-color: light-dark(#ff6b6b, #ff8a8a);
# # #         color: light-dark(#ffffff, #000000);
# # #     }
# # #     </style>
# # #     """, unsafe_allow_html=True)
# # #
# # # # Method 2: Cookie-based persistence
# # # def cookie_theme():
# # #     """Theme with cookie persistence"""
# # #     theme_js = """
# # #     <script>
# # #     function getThemeFromCookie() {
# # #         return document.cookie
# # #             .split('; ')
# # #             .find(row => row.startsWith('theme='))
# # #             ?.split('=')[1] || 'auto';
# # #     }
# # #
# # #     function setThemeCookie(theme) {
# # #         document.cookie = `theme=${theme}; path=/; max-age=31536000`; // 1 year
# # #     }
# # #
# # #     function applyTheme(theme) {
# # #         if (theme === 'auto') {
# # #             document.documentElement.removeAttribute('data-theme');
# # #         } else {
# # #             document.documentElement.setAttribute('data-theme', theme);
# # #         }
# # #     }
# # #
# # #     // Apply saved theme
# # #     const savedTheme = getThemeFromCookie();
# # #     applyTheme(savedTheme);
# # #     </script>
# # #     """
# # #     components.html(theme_js, height=0)
# # #
# # # # Method 3: URL parameter theme
# # # def url_param_theme():
# # #     """Theme based on URL parameter"""
# # #     # Get theme from URL parameter
# # #     query_params = st.experimental_get_query_params()
# # #     theme = query_params.get('theme', ['auto'])[0]
# # #
# # #     if theme == 'dark':
# # #         st.markdown("""
# # #         <style>
# # #         :root { --theme: dark; }
# # #         .stApp { background: #0e1117; color: #fafafa; }
# # #         </style>
# # #         """, unsafe_allow_html=True)
# # #     elif theme == 'light':
# # #         st.markdown("""
# # #         <style>
# # #         :root { --theme: light; }
# # #         .stApp { background: #ffffff; color: #262730; }
# # #         </style>
# # #         """, unsafe_allow_html=True)
# # #
# # #     st.write(f"Current theme: {theme}")
# # #     st.write("Try adding `?theme=dark` or `?theme=light` to the URL")
# # #
# # # # Method 4: Time-based theme
# # # def time_based_theme():
# # #     """Theme based on time of day"""
# # #     from datetime import datetime
# # #
# # #     current_hour = datetime.now().hour
# # #
# # #     # Dark theme from 7 PM to 7 AM
# # #     if current_hour >= 19 or current_hour <= 7:
# # #         is_dark = True
# # #     else:
# # #         is_dark = False
# # #
# # #     theme_css = f"""
# # #     <style>
# # #     .stApp {{
# # #         background-color: {'#0e1117' if is_dark else '#ffffff'};
# # #         color: {'#fafafa' if is_dark else '#262730'};
# # #     }}
# # #     </style>
# # #     """
# # #     st.markdown(theme_css, unsafe_allow_html=True)
# # #     st.info(f"Auto theme: {'Dark' if is_dark else 'Light'} (based on time: {current_hour}:00)")
# # #
# # # # Method 5: Custom theme component
# # # def create_theme_component():
# # #     """Create a reusable theme component"""
# # #     class ThemeManager:
# # #         def __init__(self):
# # #             self.themes = {
# # #                 'light': {
# # #                     'bg': '#ffffff',
# # #                     'secondary': '#f0f2f6',
# # #                     'text': '#262730',
# # #                     'accent': '#ff6b6b'
# # #                 },
# # #                 'dark': {
# # #                     'bg': '#0e1117',
# # #                     'secondary': '#262730',
# # #                     'text': '#fafafa',
# # #                     'accent': '#ff8a8a'
# # #                 },
# # #                 'blue': {
# # #                     'bg': '#1e3a8a',
# # #                     'secondary': '#3b82f6',
# # #                     'text': '#ffffff',
# # #                     'accent': '#fbbf24'
# # #                 }
# # #             }
# # #
# # #         def apply_theme(self, theme_name):
# # #             if theme_name not in self.themes:
# # #                 return
# # #
# # #             theme = self.themes[theme_name]
# # #             css = f"""
# # #             <style>
# # #             .stApp {{
# # #                 background-color: {theme['bg']};
# # #                 color: {theme['text']};
# # #             }}
# # #             .stSidebar {{
# # #                 background-color: {theme['secondary']};
# # #             }}
# # #             .stButton > button {{
# # #                 background-color: {theme['accent']};
# # #                 color: white;
# # #             }}
# # #             </style>
# # #             """
# # #             st.markdown(css, unsafe_allow_html=True)
# # #
# # #         def theme_selector(self):
# # #             return st.selectbox(
# # #                 "Choose Theme",
# # #                 list(self.themes.keys()),
# # #                 key="theme_selector"
# # #             )
# # #
# # # # Usage example
# # # def demo_theme_manager():
# # #     tm = ThemeManager()
# # #     selected_theme = tm.theme_selector()
# # #     tm.apply_theme(selected_theme)
# # #
# # #     st.title("Custom Theme Manager Demo")
# # #     st.write(f"Current theme: {selected_theme}")
# #
# #
# # import streamlit as st
# #
# # def apply_dynamic_theme():
# #     """Simple CSS-only dynamic theme that responds to browser preference"""
# #     theme_css = """
# #     <style>
# #     /* Variables for light mode (default) */
# #     :root {
# #         --primary-bg: #ffffff;
# #         --secondary-bg: #f0f2f6;
# #         --text-color: #262730;
# #         --accent-color: #F39C12;
# #         --border-color: #e0e0e0;
# #         --sidebar-bg: #f8f9fa;
# #     }
# #
# #     /* Dark mode - automatically applied when browser is in dark mode */
# #     @media (prefers-color-scheme: dark) {
# #         :root {
# #             --primary-bg: #14131f;
# #             --secondary-bg: #1e1d2e;
# #             --text-color: #ffffff;
# #             --accent-color: #F39C12;
# #             --border-color: #333333;
# #             --sidebar-bg: #262730;
# #         }
# #     }
# #
# #     /* Apply theme to Streamlit elements */
# #     .stApp {
# #         background-color: var(--primary-bg) !important;
# #         color: var(--text-color) !important;
# #     }
# #
# #     .stApp > header {
# #         background-color: transparent !important;
# #     }
# #
# #     .stApp > div:first-child {
# #         background-color: var(--primary-bg) !important;
# #     }
# #
# #     /* Sidebar */
# #     section[data-testid="stSidebar"] {
# #         background-color: var(--sidebar-bg) !important;
# #     }
# #
# #     section[data-testid="stSidebar"] > div {
# #         background-color: var(--sidebar-bg) !important;
# #     }
# #
# #     /* Input elements */
# #     .stTextInput input, .stTextArea textarea, .stSelectbox select {
# #         background-color: var(--secondary-bg) !important;
# #         color: var(--text-color) !important;
# #         border-color: var(--border-color) !important;
# #     }
# #
# #     .stSelectbox > div > div {
# #         background-color: var(--secondary-bg) !important;
# #         color: var(--text-color) !important;
# #     }
# #
# #     /* Buttons */
# #     .stButton > button {
# #         background-color: var(--accent-color) !important;
# #         color: white !important;
# #         border: none !important;
# #         border-radius: 5px !important;
# #     }
# #
# #     .stButton > button:hover {
# #         opacity: 0.8 !important;
# #     }
# #
# #     /* Metrics */
# #     div[data-testid="metric-container"] {
# #         background-color: var(--secondary-bg) !important;
# #         border: 1px solid var(--border-color) !important;
# #         border-radius: 10px !important;
# #         padding: 1rem !important;
# #     }
# #
# #     /* Dataframes */
# #     .stDataFrame {
# #         background-color: var(--secondary-bg) !important;
# #     }
# #
# #     /* Markdown */
# #     .stMarkdown {
# #         color: var(--text-color) !important;
# #     }
# #
# #     /* Success/Error/Warning messages */
# #     .stAlert {
# #         background-color: var(--secondary-bg) !important;
# #         border-color: var(--border-color) !important;
# #         color: var(--text-color) !important;
# #     }
# #
# #     /* Charts background */
# #     .js-plotly-plot, .plotly {
# #         background-color: var(--primary-bg) !important;
# #     }
# #
# #     /* Tabs */
# #     .stTabs [data-baseweb="tab-list"] {
# #         background-color: var(--secondary-bg) !important;
# #     }
# #
# #     .stTabs [data-baseweb="tab"] {
# #         color: var(--text-color) !important;
# #     }
# #
# #     /* Expander */
# #     .streamlit-expanderHeader {
# #         background-color: var(--secondary-bg) !important;
# #         color: var(--text-color) !important;
# #     }
# #     </style>
# #     """
# #     st.markdown(theme_css, unsafe_allow_html=True)
# #
# # def add_manual_theme_toggle():
# #     """Optional: Add manual theme override without JavaScript"""
# #     if 'manual_theme' not in st.session_state:
# #         st.session_state.manual_theme = 'auto'
# #
# #     # Theme selector in sidebar
# #     with st.sidebar:
# #         theme_choice = st.radio(
# #             "🎨 Theme",
# #             ['auto', 'light', 'dark'],
# #             index=['auto', 'light', 'dark'].index(st.session_state.manual_theme),
# #             help="Auto follows your browser/system preference"
# #         )
# #         st.session_state.manual_theme = theme_choice
# #
# #     # Apply manual override if needed
# #     if theme_choice == 'light':
# #         st.markdown("""
# #         <style>
# #         :root {
# #             --primary-bg: #ffffff !important;
# #             --secondary-bg: #f0f2f6 !important;
# #             --text-color: #262730 !important;
# #             --sidebar-bg: #f8f9fa !important;
# #         }
# #         </style>
# #         """, unsafe_allow_html=True)
# #     elif theme_choice == 'dark':
# #         st.markdown("""
# #         <style>
# #         :root {
# #             --primary-bg: #14131f !important;
# #             --secondary-bg: #1e1d2e !important;
# #             --text-color: #ffffff !important;
# #             --sidebar-bg: #262730 !important;
# #         }
# #         </style>
# #         """, unsafe_allow_html=True)
# #
# # # Demo app
# # def main():
# #     st.set_page_config(
# #         page_title="Dynamic Theme Demo",
# #         page_icon="🌙",
# #         layout="wide",
# #         initial_sidebar_state="expanded"
# #     )
# #
# #     # Apply the dynamic theme (this is the key part!)
# #     apply_dynamic_theme()
# #
# #     # Optional manual toggle
# #     add_manual_theme_toggle()
# #
# #     # Your app content
# #     st.title("🌙 Dynamic Theme Demo")
# #     st.write("This automatically switches between light and dark based on your browser/system settings!")
# #
# #     col1, col2, col3 = st.columns(3)
# #     with col1:
# #         st.metric("Users", "1,234", "+12%")
# #     with col2:
# #         st.metric("Revenue", "$45K", "+8%")
# #     with col3:
# #         st.metric("Growth", "23%", "+5%")
# #
# #     st.subheader("Test Elements")
# #
# #     name = st.text_input("Enter your name", placeholder="John Doe")
# #     option = st.selectbox("Choose option", ["Option 1", "Option 2", "Option 3"])
# #
# #     if st.button("Test Button"):
# #         st.success(f"Hello {name}! You selected {option}")
# #         if option == "Option 1":
# #                     st.info("ℹ️ You chose Option 1 - This is an info message!")
# #         elif option == "Option 2":
# #                     st.warning("⚠️ You chose Option 2 - This is a warning message!")
# #         elif option == "Option 3":
# #                     st.error("❌ You chose Option 3 - This is an error message!")
# #
# #
# #     # Test expander
# #     with st.expander("Click to expand"):
# #         st.write("This content is inside an expander!")
# #
# #     # Test tabs
# #     tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
# #     with tab1:
# #         st.write("Content in tab 1")
# #     with tab2:
# #         st.write("Content in tab 2")
# #
# #     st.markdown("---")
# #     st.markdown("""
# #     ### How to use in your app:
# #
# #     1. Copy the `apply_dynamic_theme()` function
# #     2. Call it at the start of your app (after `st.set_page_config`)
# #     3. That's it! No JavaScript, no blank screens.
# #
# #     **The theme will automatically switch when you:**
# #     - Change your system theme (Windows/Mac/Linux)
# #     - Change browser theme preference
# #     - Use browser dev tools to toggle dark mode
# #     """)
# #
# # if __name__ == "__main__":
# #     main()
#
#
# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from datetime import datetime, date
# import json
#
# # Configuration
# API_BASE_URL = "http://localhost:8000"
#
# def apply_dynamic_theme():
#     """Dynamic theme that responds to browser preference"""
#     theme_css = """
#     <style>
#     :root {
#         --primary-bg: #ffffff;
#         --secondary-bg: #f0f2f6;
#         --text-color: #262730;
#         --accent-color: #F39C12;
#         --border-color: #e0e0e0;
#         --sidebar-bg: #f8f9fa;
#         --success-color: #28a745;
#         --warning-color: #ffc107;
#         --error-color: #dc3545;
#     }
#
#     @media (prefers-color-scheme: dark) {
#         :root {
#             --primary-bg: #14131f;
#             --secondary-bg: #1e1d2e;
#             --text-color: #ffffff;
#             --accent-color: #F39C12;
#             --border-color: #333333;
#             --sidebar-bg: #262730;
#             --success-color: #28a745;
#             --warning-color: #ffc107;
#             --error-color: #dc3545;
#         }
#     }
#
#     .stApp {
#         background-color: var(--primary-bg) !important;
#         color: var(--text-color) !important;
#     }
#
#     section[data-testid="stSidebar"] {
#         background-color: var(--sidebar-bg) !important;
#     }
#
#     .stSelectbox > div > div, .stTextInput input, .stTextArea textarea {
#         background-color: var(--secondary-bg) !important;
#         color: var(--text-color) !important;
#         border-color: var(--border-color) !important;
#     }
#
#     .stButton > button {
#         background-color: var(--accent-color) !important;
#         color: white !important;
#         border: none !important;
#         border-radius: 5px !important;
#     }
#
#     .stButton > button:hover {
#         opacity: 0.8 !important;
#     }
#
#     div[data-testid="metric-container"] {
#         background-color: var(--secondary-bg) !important;
#         border: 1px solid var(--border-color) !important;
#         border-radius: 10px !important;
#         padding: 1rem !important;
#     }
#
#     .stDataFrame {
#         background-color: var(--secondary-bg) !important;
#     }
#
#     .stAlert {
#         background-color: var(--secondary-bg) !important;
#         border-color: var(--border-color) !important;
#         color: var(--text-color) !important;
#     }
#
#     .js-plotly-plot, .plotly {
#         background-color: var(--primary-bg) !important;
#     }
#
#     /* Custom card styling */
#     .metric-card {
#         background-color: var(--secondary-bg);
#         padding: 1rem;
#         border-radius: 10px;
#         border: 1px solid var(--border-color);
#         margin: 0.5rem 0;
#     }
#     </style>
#     """
#     st.markdown(theme_css, unsafe_allow_html=True)
#
# def check_api_health():
#     """Check if API is running"""
#     try:
#         response = requests.get(f"{API_BASE_URL}/health", timeout=5)
#         return response.status_code == 200
#     except:
#         return False
#
# def get_data(endpoint, params=None):
#     """Generic function to fetch data from API"""
#     try:
#         response = requests.get(f"{API_BASE_URL}{endpoint}", params=params, timeout=10)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             st.error(f"API Error: {response.status_code}")
#             return None
#     except requests.exceptions.ConnectionError:
#         st.error("🔌 Cannot connect to API. Make sure FastAPI server is running!")
#         return None
#     except Exception as e:
#         st.error(f"Error: {str(e)}")
#         return None
#
# def post_data(endpoint, data):
#     """Generic function to post data to API"""
#     try:
#         response = requests.post(
#             f"{API_BASE_URL}{endpoint}",
#             json=data,
#             headers={"Content-Type": "application/json"},
#             timeout=10
#         )
#         if response.status_code in [200, 201]:
#             return response.json()
#         else:
#             st.error(f"API Error: {response.status_code} - {response.text}")
#             return None
#     except Exception as e:
#         st.error(f"Error: {str(e)}")
#         return None
#
# def display_dashboard():
#     """Display main dashboard with summary statistics"""
#     st.subheader("📊 Dashboard Overview")
#
#     # Get dashboard data
#     summary_data = get_data("/dashboard/summary")
#
#     if summary_data:
#         # Display key metrics
#         col1, col2, col3, col4 = st.columns(4)
#
#         order_stats = summary_data.get("order_stats", {})
#
#         with col1:
#             total_orders = order_stats.get("total_orders", 0)
#             st.metric("Total Orders", f"{total_orders:,}")
#
#         with col2:
#             total_revenue = order_stats.get("total_revenue", 0)
#             st.metric("Total Revenue", f"${total_revenue:,.2f}")
#
#         with col3:
#             avg_order = order_stats.get("avg_order_value", 0)
#             st.metric("Avg Order Value", f"${avg_order:.2f}")
#
#         with col4:
#             unique_customers = order_stats.get("unique_customers", 0)
#             st.metric("Unique Customers", f"{unique_customers:,}")
#
#         # Department statistics chart
#         dept_stats = summary_data.get("department_stats", [])
#         if dept_stats:
#             col1, col2 = st.columns(2)
#
#             with col1:
#                 st.subheader("👥 Staff by Department")
#                 dept_df = pd.DataFrame(dept_stats)
#                 fig_dept = px.pie(dept_df, values='count', names='department',
#                                 title="Employee Distribution")
#                 fig_dept.update_layout(
#                     plot_bgcolor='rgba(1,1,1,10)',
#                     paper_bgcolor='rgba(1,0,0,0)',
#                 )
#                 st.plotly_chart(fig_dept, use_container_width=True)
#
#             with col2:
#                 st.subheader("💰 Average Salary by Dept")
#                 fig_salary = px.bar(dept_df, x='department', y='avg_salary',
#                                   title="Average Salary by Department")
#                 fig_salary.update_layout(
#                     plot_bgcolor='rgba(0,1,0,0.1)',
#                     paper_bgcolor='rgba(0,1,0,0)',
#                 )
#                 st.plotly_chart(fig_salary, use_container_width=True)
#
#         # Revenue by category
#         revenue_data = get_data("/dashboard/revenue-by-category")
#         if revenue_data:
#             st.subheader("💳 Revenue by Product Category")
#             revenue_df = pd.DataFrame(revenue_data)
#
#             col1, col2 = st.columns(2)
#             with col1:
#                 fig_revenue = px.bar(revenue_df, x='product_category', y='total_revenue',
#                                    title="Total Revenue by Category")
#                 fig_revenue.update_layout(
#                     plot_bgcolor='rgba(0,0,0,0)',
#                     paper_bgcolor='rgba(0,0,0,0)',
#                 )
#                 st.plotly_chart(fig_revenue, use_container_width=True)
#
#             with col2:
#                 st.write("**Revenue Summary Table**")
#                 st.dataframe(
#                     revenue_df[['product_category', 'total_revenue', 'order_count']]
#                     .round(2),
#                     use_container_width=True
#                 )
#
# def display_users():
#     """Display and manage users"""
#     st.subheader("👥 User Management")
#
#     # Get users
#     users_data = get_data("/users")
#
#     if users_data:
#         users_df = pd.DataFrame(users_data)
#
#         # Display users table
#         st.write("**Current Users**")
#         display_df = users_df[['user_id', 'full_name', 'email', 'department', 'salary']].copy()
#         display_df['salary'] = display_df['salary'].apply(lambda x: f"${x:,.2f}")
#         st.data_editor(display_df, use_container_width=True)
#
#         # Add new user form
#         with st.expander("➕ Add New User"):
#             with st.form("add_user_form", clear_on_submit=True):
#                 col1, col2 = st.columns(2)
#
#                 with col1:
#                     username = st.text_input("Username*")
#                     full_name = st.text_input("Full Name*")
#                     email = st.text_input("Email*")
#
#                 with col2:
#                     department = st.selectbox("Department*",
#                         ["Engineering", "Marketing", "Sales", "HR", "Finance", "Operations"])
#                     salary = st.number_input("Salary*", min_value=0.0, step=1000.0, value=50000.0)
#
#                 submitted = st.form_submit_button("Add User")
#
#                 if submitted:
#                     if username and full_name and email:
#                         user_data = {
#                             "username": username,
#                             "full_name": full_name,
#                             "email": email,
#                             "department": department,
#                             "salary": salary
#                         }
#
#                         result = post_data("/users", user_data)
#                         if result:
#                             st.success(f"✅ User {full_name} added successfully!")
#                             st.rerun()
#                         else:
#                             st.error("❌ Failed to add user")
#                     else:
#                         st.error("Please fill in all required fields")
#
# def display_orders():
#     """Display and manage orders"""
#     st.subheader("🛒 Order Management")
#
#     # Get orders
#     orders_data = get_data("/orders")
#
#     if orders_data:
#         orders_df = pd.DataFrame(orders_data)
#
#         # Display orders table
#         st.write("**Recent Orders**")
#         display_df = orders_df[['order_id', 'user_id', 'total_amount', 'status',
#                                'product_category', 'quantity', 'order_date']].copy()
#         display_df['total_amount'] = display_df['total_amount'].apply(lambda x: f"${x:,.2f}")
#         st.dataframe(display_df, use_container_width=True)
#
#         # Add new order form
#         users_data = get_data("/users")
#         if users_data:
#             with st.expander("➕ Add New Order"):
#                 with st.form("add_order_form"):
#                     col1, col2 = st.columns(2)
#
#                     with col1:
#                         # Create user selectbox
#                         user_options = {f"{user['full_name']} (ID: {user['user_id']})": user['user_id']
#                                       for user in users_data}
#                         selected_user = st.selectbox("Select User*", options=list(user_options.keys()))
#                         user_id = user_options[selected_user]
#
#                         product_category = st.selectbox("Product Category*",
#                             ["Electronics", "Books", "Clothing", "Home", "Sports"])
#
#                     with col2:
#                         total_amount = st.number_input("Total Amount*", min_value=0.0, step=1.0, value=99.99)
#                         quantity = st.number_input("Quantity*", min_value=1, step=1, value=1)
#                         status = st.selectbox("Status", ["pending", "completed", "shipped", "cancelled"])
#
#                     submitted = st.form_submit_button("Add Order")
#
#                     if submitted:
#                         order_data = {
#                             "user_id": user_id,
#                             "total_amount": total_amount,
#                             "status": status,
#                             "product_category": product_category,
#                             "quantity": quantity
#                         }
#
#                         result = post_data("/orders", order_data)
#                         if result:
#                             st.success(f"✅ Order added successfully!")
#                             st.rerun()
#                         else:
#                             st.error("❌ Failed to add order")
#
# def display_analytics():
#     """Display analytics data"""
#     st.subheader("📈 Analytics Dashboard")
#
#     # Get page views data
#     analytics_data = get_data("/analytics/page-views")
#
#     if analytics_data:
#         analytics_df = pd.DataFrame(analytics_data)
#
#         # Page views over time
#         st.write("**Page Views Over Time**")
#
#         # Group by date and sum views
#         daily_views = analytics_df.groupby('view_date').agg({
#             'views': 'sum',
#             'unique_visitors': 'sum',
#             'bounce_rate': 'mean'
#         }).reset_index()
#
#         col1, col2 = st.columns(2)
#
#         with col1:
#             fig_views = px.line(daily_views, x='view_date', y='views',
#                               title="Total Daily Page Views")
#             fig_views.update_layout(
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 paper_bgcolor='rgba(0,0,0,0)',
#             )
#             st.plotly_chart(fig_views, use_container_width=True)
#
#         with col2:
#             fig_bounce = px.line(daily_views, x='view_date', y='bounce_rate',
#                                title="Average Bounce Rate")
#             fig_bounce.update_layout(
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 paper_bgcolor='rgba(0,0,0,0)',
#             )
#             st.plotly_chart(fig_bounce, use_container_width=True)
#
#         # Page performance
#         page_perf = analytics_df.groupby('page_name').agg({
#             'views': 'sum',
#             'unique_visitors': 'sum',
#             'bounce_rate': 'mean'
#         }).reset_index().sort_values('views', ascending=False)
#
#         st.write("**Page Performance Summary**")
#         st.dataframe(page_perf, use_container_width=True)
#
# def main():
#     st.set_page_config(
#         page_title="FastAPI + PostgreSQL Dashboard",
#         page_icon="🚀",
#         layout="wide",
#         initial_sidebar_state="expanded"
#     )
#
#     # Apply dynamic theme
#     apply_dynamic_theme()
#
#     # Header
#     st.title("🚀 FastAPI + PostgreSQL Dashboard")
#
#     # Check API health
#     if not check_api_health():
#         st.error("🔌 **API Connection Failed!** Make sure your FastAPI server is running on http://localhost:8000")
#         st.info("Run: `uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000`")
#         return
#
#     st.success("✅ Connected to FastAPI backend")
#
#     # Sidebar navigation
#     with st.sidebar:
#         st.header("Navigation")
#         page = st.radio(
#             "Go to:",
#             ["Dashboard", "Users", "Orders", "Analytics"],
#             label_visibility="collapsed"
#         )
#
#         st.markdown("---")
#         st.markdown("### API Status")
#         if check_api_health():
#             st.success("🟢 API Online")
#         else:
#             st.error("🔴 API Offline")
#
#         st.markdown("---")
#         st.markdown("### Quick Stats")
#
#         # Quick stats
#         summary = get_data("/dashboard/summary")
#         if summary:
#             order_stats = summary.get("order_stats", {})
#             st.metric("Orders", order_stats.get("total_orders", "—"))
#             st.metric("Revenue", f"${order_stats.get('total_revenue', 0):,.0f}")
#
#     # Main content based on selection
#     if page == "Dashboard":
#         display_dashboard()
#     elif page == "Users":
#         display_users()
#     elif page == "Orders":
#         display_orders()
#     elif page == "Analytics":
#         display_analytics()
#
# if __name__ == "__main__":
#     main()


import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import json

# Configuration
API_BASE_URL = "http://localhost:8000"

def apply_dynamic_theme():
    """Dynamic theme that responds to browser preference"""
    theme_css = """
    <style>
    :root {
        --primary-bg: #ffffff;
        --secondary-bg: #f0f2f6;
        --text-color: #262730;
        --accent-color: #F39C12;
        --border-color: #e0e0e0;
        --sidebar-bg: #f8f9fa;
        --success-color: #28a745;
        --warning-color: #ffc107;
        --error-color: #dc3545;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --primary-bg: #14131f;
            --secondary-bg: #1e1d2e;
            --text-color: #ffffff;
            --accent-color: #F39C12;
            --border-color: #333333;
            --sidebar-bg: #262730;
            --success-color: #28a745;
            --warning-color: #ffc107;
            --error-color: #dc3545;
        }
    }

    .stApp {
        background-color: var(--primary-bg) !important;
        color: var(--text-color) !important;
    }

    section[data-testid="stSidebar"] {
        background-color: var(--sidebar-bg) !important;
    }

    .stSelectbox > div > div, .stTextInput input, .stTextArea textarea {
        background-color: var(--secondary-bg) !important;
        color: var(--text-color) !important;
        border-color: var(--border-color) !important;
    }

    .stButton > button {
        background-color: var(--accent-color) !important;
        color: white !important;
        border: none !important;
        border-radius: 5px !important;
    }

    .stButton > button:hover {
        opacity: 0.8 !important;
    }

    div[data-testid="metric-container"] {
        background-color: var(--secondary-bg) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
    }

    .stDataFrame {
        background-color: var(--secondary-bg) !important;
    }

    .stAlert {
        background-color: var(--secondary-bg) !important;
        border-color: var(--border-color) !important;
        color: var(--text-color) !important;
    }

    .js-plotly-plot, .plotly {
        background-color: var(--primary-bg) !important;
    }

    /* Custom card styling */
    .metric-card {
        background-color: var(--secondary-bg);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid var(--border-color);
        margin: 0.5rem 0;
    }
    </style>
    """
    st.markdown(theme_css, unsafe_allow_html=True)

def check_api_health():
    """Check if API is running"""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def get_data(endpoint, params=None):
    """Generic function to fetch data from API"""
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Error: {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        st.error("🔌 Cannot connect to API. Make sure FastAPI server is running!")
        return None
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def post_data(endpoint, data):
    """Generic function to post data to API"""
    try:
        response = requests.post(
            f"{API_BASE_URL}{endpoint}",
            json=data,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        if response.status_code in [200, 201]:
            return response.json()
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def display_dashboard():
    """Display main dashboard with summary statistics"""
    st.subheader("📊 Dashboard Overview")

    # Get dashboard data
    summary_data = get_data("/dashboard/summary")

    if summary_data:
        # Display key metrics
        col1, col2, col3, col4 = st.columns(4)

        order_stats = summary_data.get("order_stats", {})

        with col1:
            total_orders = order_stats.get("total_orders", 0)
            st.metric("Total Orders", f"{total_orders:,}")

        with col2:
            total_revenue = order_stats.get("total_revenue", 0)
            st.metric("Total Revenue", f"${total_revenue:,.2f}")

        with col3:
            avg_order = order_stats.get("avg_order_value", 0)
            st.metric("Avg Order Value", f"${avg_order:.2f}")

        with col4:
            unique_customers = order_stats.get("unique_customers", 0)
            st.metric("Unique Customers", f"{unique_customers:,}")

        # Department statistics chart
        dept_stats = summary_data.get("department_stats", [])
        if dept_stats:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("👥 Staff by Department")
                dept_df = pd.DataFrame(dept_stats)
                fig_dept = px.pie(dept_df, values='count', names='department',
                                title="Employee Distribution")
                fig_dept.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                )
                st.plotly_chart(fig_dept, use_container_width=True)

            with col2:
                st.subheader("💰 Average Salary by Dept")
                fig_salary = px.bar(dept_df, x='department', y='avg_salary',
                                  title="Average Salary by Department")
                fig_salary.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                )
                st.plotly_chart(fig_salary, use_container_width=True)

        # Revenue by category
        revenue_data = get_data("/dashboard/revenue-by-category")
        if revenue_data:
            st.subheader("💳 Revenue by Product Category")
            revenue_df = pd.DataFrame(revenue_data)

            col1, col2 = st.columns(2)
            with col1:
                fig_revenue = px.bar(revenue_df, x='product_category', y='total_revenue',
                                   title="Total Revenue by Category")
                fig_revenue.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                )
                st.plotly_chart(fig_revenue, use_container_width=True)

            with col2:
                st.write("**Revenue Summary Table**")
                st.dataframe(
                    revenue_df[['product_category', 'total_revenue', 'order_count']]
                    .round(2),
                    use_container_width=True
                )

def put_data(endpoint, data):
    """Generic function to update data via API"""
    try:
        response = requests.put(
            f"{API_BASE_URL}{endpoint}",
            json=data,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def display_users():
    """Display and manage users with editable data editor"""
    st.subheader("👥 User Management")

    # Get users
    users_data = get_data("/users")

    if users_data:
        users_df = pd.DataFrame(users_data)

        # Prepare data for editing - keep original format for editing
        edit_df = users_df[['user_id', 'username', 'full_name', 'email', 'department', 'salary']].copy()

        st.write("**Edit Users** (Double-click cells to edit, then press Enter)")

        # Configure column settings for the data editor
        column_config = {
            "user_id": st.column_config.NumberColumn(
                "ID",
                help="User ID (read-only)",
                disabled=True,
                width="small"
            ),
            "username": st.column_config.TextColumn(
                "Username",
                help="Unique username",
                max_chars=50,
                width="medium"
            ),
            "full_name": st.column_config.TextColumn(
                "Full Name",
                help="User's full name",
                max_chars=100,
                width="medium"
            ),
            "email": st.column_config.TextColumn(
                "Email",
                help="Email address",
                max_chars=100,
                width="medium"
            ),
            "department": st.column_config.SelectboxColumn(
                "Department",
                help="Select department",
                width="medium",
                options=["Engineering", "Marketing", "Sales", "HR", "Finance", "Operations"]
            ),
            "salary": st.column_config.NumberColumn(
                "Salary",
                help="Annual salary in USD",
                min_value=0,
                max_value=1000000,
                step=1000,
                format="$%.2f",
                width="medium"
            )
        }

        # Use data_editor for inline editing
        edited_df = st.data_editor(
            edit_df,
            column_config=column_config,
            use_container_width=True,
            num_rows="fixed",  # Don't allow adding/deleting rows
            key="users_editor"
        )

        # Check for changes and provide update button
        if not edit_df.equals(edited_df):
            st.info("📝 You have unsaved changes!")

            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("💾 Save Changes", type="primary"):
                    # Find changed rows
                    changes_made = 0
                    errors = 0

                    for idx in edited_df.index:
                        original_row = edit_df.iloc[idx]
                        edited_row = edited_df.iloc[idx]

                        # Check if this row was changed
                        if not original_row.equals(edited_row):
                            user_id = int(edited_row['user_id'])

                            # Prepare update data
                            update_data = {
                                "username": edited_row['username'],
                                "email": edited_row['email'],
                                "full_name": edited_row['full_name'],
                                "department": edited_row['department'],
                                "salary": float(edited_row['salary'])
                            }

                            # Update via API
                            result = put_data(f"/users/{user_id}", update_data)
                            if result:
                                changes_made += 1
                            else:
                                errors += 1

                    # Show results
                    if changes_made > 0:
                        st.success(f"✅ Successfully updated {changes_made} user(s)!")
                        if errors == 0:
                            st.rerun()  # Refresh the page to show updated data

                    if errors > 0:
                        st.error(f"❌ Failed to update {errors} user(s)")

            with col2:
                if st.button("🔄 Reset Changes"):
                    st.rerun()

        # Show summary statistics
        st.markdown("---")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Users", len(users_df))

        with col2:
            avg_salary = users_df['salary'].mean()
            st.metric("Average Salary", f"${avg_salary:,.0f}")

        with col3:
            dept_count = users_df['department'].nunique()
            st.metric("Departments", dept_count)

        # Add new user form
        with st.expander("➕ Add New User"):
            with st.form("add_user_form"):
                col1, col2 = st.columns(2)

                with col1:
                    username = st.text_input("Username*")
                    full_name = st.text_input("Full Name*")
                    email = st.text_input("Email*")

                with col2:
                    department = st.selectbox("Department*",
                        ["Engineering", "Marketing", "Sales", "HR", "Finance", "Operations"])
                    salary = st.number_input("Salary*", min_value=0.0, step=1000.0, value=50000.0)

                submitted = st.form_submit_button("Add User")

                if submitted:
                    if username and full_name and email:
                        user_data = {
                            "username": username,
                            "full_name": full_name,
                            "email": email,
                            "department": department,
                            "salary": salary
                        }

                        result = post_data("/users", user_data)
                        if result:
                            st.success(f"✅ User {full_name} added successfully!")
                            st.rerun()
                        else:
                            st.error("❌ Failed to add user")
                    else:
                        st.error("Please fill in all required fields")

def display_orders():
    """Display and manage orders"""
    st.subheader("🛒 Order Management")

    # Get orders
    orders_data = get_data("/orders")

    if orders_data:
        orders_df = pd.DataFrame(orders_data)

        # Display orders table
        st.write("**Recent Orders**")
        display_df = orders_df[['order_id', 'user_id', 'total_amount', 'status',
                               'product_category', 'quantity', 'order_date']].copy()
        display_df['total_amount'] = display_df['total_amount'].apply(lambda x: f"${x:,.2f}")
        st.dataframe(display_df, use_container_width=True)

        # Add new order form
        users_data = get_data("/users")
        if users_data:
            with st.expander("➕ Add New Order"):
                with st.form("add_order_form"):
                    col1, col2 = st.columns(2)

                    with col1:
                        # Create user selectbox
                        user_options = {f"{user['full_name']} (ID: {user['user_id']})": user['user_id']
                                      for user in users_data}
                        selected_user = st.selectbox("Select User*", options=list(user_options.keys()))
                        user_id = user_options[selected_user]

                        product_category = st.selectbox("Product Category*",
                            ["Electronics", "Books", "Clothing", "Home", "Sports"])

                    with col2:
                        total_amount = st.number_input("Total Amount*", min_value=0.0, step=1.0, value=99.99)
                        quantity = st.number_input("Quantity*", min_value=1, step=1, value=1)
                        status = st.selectbox("Status", ["pending", "completed", "shipped", "cancelled"])

                    submitted = st.form_submit_button("Add Order")

                    if submitted:
                        order_data = {
                            "user_id": user_id,
                            "total_amount": total_amount,
                            "status": status,
                            "product_category": product_category,
                            "quantity": quantity
                        }

                        result = post_data("/orders", order_data)
                        if result:
                            st.success(f"✅ Order added successfully!")
                            st.rerun()
                        else:
                            st.error("❌ Failed to add order")

def display_analytics():
    """Display analytics data"""
    st.subheader("📈 Analytics Dashboard")

    # Get page views data
    analytics_data = get_data("/analytics/page-views")

    if analytics_data:
        analytics_df = pd.DataFrame(analytics_data)

        # Page views over time
        st.write("**Page Views Over Time**")

        # Group by date and sum views
        daily_views = analytics_df.groupby('view_date').agg({
            'views': 'sum',
            'unique_visitors': 'sum',
            'bounce_rate': 'mean'
        }).reset_index()

        col1, col2 = st.columns(2)

        with col1:
            fig_views = px.line(daily_views, x='view_date', y='views',
                              title="Total Daily Page Views")
            fig_views.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
            )
            st.plotly_chart(fig_views, use_container_width=True)

        with col2:
            fig_bounce = px.line(daily_views, x='view_date', y='bounce_rate',
                               title="Average Bounce Rate")
            fig_bounce.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
            )
            st.plotly_chart(fig_bounce, use_container_width=True)

        # Page performance
        page_perf = analytics_df.groupby('page_name').agg({
            'views': 'sum',
            'unique_visitors': 'sum',
            'bounce_rate': 'mean'
        }).reset_index().sort_values('views', ascending=False)

        st.write("**Page Performance Summary**")
        st.dataframe(page_perf, use_container_width=True)

def main():
    st.set_page_config(
        page_title="FastAPI + PostgreSQL Dashboard",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Apply dynamic theme
    apply_dynamic_theme()

    # Header
    st.title("🚀 FastAPI + PostgreSQL Dashboard")

    # Check API health
    if not check_api_health():
        st.error("🔌 **API Connection Failed!** Make sure your FastAPI server is running on http://localhost:8000")
        st.info("Run: `uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000`")
        return

    st.success("✅ Connected to FastAPI backend")

    # Sidebar navigation
    with st.sidebar:
        st.header("Navigation")
        page = st.radio(
            "Go to:",
            ["Dashboard", "Users", "Orders", "Analytics"],
            label_visibility="collapsed"
        )

        st.markdown("---")
        st.markdown("### API Status")
        if check_api_health():
            st.success("🟢 API Online")
        else:
            st.error("🔴 API Offline")

        st.markdown("---")
        st.markdown("### Quick Stats")

        # Quick stats
        summary = get_data("/dashboard/summary")
        if summary:
            order_stats = summary.get("order_stats", {})
            st.metric("Orders", order_stats.get("total_orders", "—"))
            st.metric("Revenue", f"${order_stats.get('total_revenue', 0):,.0f}")

    # Main content based on selection
    if page == "Dashboard":
        display_dashboard()
    elif page == "Users":
        display_users()
    elif page == "Orders":
        display_orders()
    elif page == "Analytics":
        display_analytics()

if __name__ == "__main__":
    main()
