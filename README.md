# 🚀 FastAPI + PostgreSQL + Streamlit Dashboard

A modern full-stack web application built with FastAPI, PostgreSQL, and Streamlit featuring a dynamic dark/light theme and real-time data management.

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue.svg)

## ✨ Features

- 🎨 **Dynamic Theme**: Automatically adapts to browser dark/light mode preference
- 📊 **Interactive Dashboard**: Real-time metrics and visualizations with Plotly
- 👥 **User Management**: Full CRUD operations with inline editing using `st.data_editor`
- 🛒 **Order Management**: Create and track orders with user relationships
- 📈 **Analytics Dashboard**: Page views, bounce rates, and performance metrics
- 🔄 **Real-time Updates**: Live data synchronization between frontend and backend
- 🚀 **Modern Stack**: FastAPI + PostgreSQL + Streamlit with UV package management
- 🌐 **RESTful API**: Complete API with auto-generated documentation
- 🔐 **Error Handling**: Comprehensive error handling and user feedback

## 🏗️ Architecture

```
┌─────────────────┐    HTTP/REST    ┌─────────────────┐    SQL    ┌─────────────────┐
│                 │ ◄──────────────► │                 │ ◄────────► │                 │
│   Streamlit     │                 │     FastAPI     │           │   PostgreSQL    │
│   (Frontend)    │                 │    (Backend)    │           │   (Database)    │
│                 │                 │                 │           │                 │
└─────────────────┘                 └─────────────────┘           └─────────────────┘
        │                                    │                            │
        ▼                                    ▼                            ▼
• Dynamic theming                    • REST API endpoints           • Users table
• Interactive charts                 • Data validation              • Orders table
• Real-time updates                  • CRUD operations              • Analytics table
• Inline data editing               • Auto documentation           • Sample data
```

## 📋 Prerequisites

- **Python 3.11+**
- **Docker** (for PostgreSQL)
- **UV** package manager by Astral

## ⚡ Quick Start

### 1. Install UV (if not already installed)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Setup PostgreSQL Database

```bash
# Run PostgreSQL with Docker
docker run --name postgres_postgres_1 -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:15

# Create database and tables
docker exec -it postgres_postgres_1 psql -U postgres -c "
CREATE DATABASE streamlit_demo;
CREATE USER streamlit_user WITH PASSWORD 'streamlit123';
GRANT ALL PRIVILEGES ON DATABASE streamlit_demo TO streamlit_user;
"

# Copy and run the setup SQL file (provided in repository)
docker cp setup_streamlit_db.sql postgres_postgres_1:/tmp/
docker exec -it postgres_postgres_1 psql -U postgres -f /tmp/setup_streamlit_db.sql
```

### 3. Clone and Setup Project

```bash
# Clone repository
git clone <repository-url>
cd fastapi-postgres-streamlit

# Initialize UV project
uv init --name fastapi-postgres-app --python 3.11

# Install dependencies
uv add fastapi "uvicorn[standard]" psycopg2-binary pydantic python-multipart streamlit pandas plotly requests
```

### 4. Run the Application

**Terminal 1 - FastAPI Backend:**
```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Streamlit Frontend:**
```bash
uv run streamlit run streamlit_app.py --server.port 8501
```

### 5. Access the Application

- **Streamlit Dashboard**: http://localhost:8501
- **FastAPI Documentation**: http://localhost:8000/docs
- **API Health Check**: http://localhost:8000/health

## 📁 Project Structure

```
fastapi-postgres-streamlit/
├── main.py                 # FastAPI application
├── streamlit_app.py        # Streamlit dashboard
├── setup_streamlit_db.sql  # Database setup script
├── pyproject.toml          # Project configuration
├── README.md              # This file
├── .venv/                 # Virtual environment (created by UV)
└── screenshots/           # Application screenshots
```

## 🎯 Application Pages

### 📊 Dashboard
- **Key Metrics**: Total orders, revenue, average order value, unique customers
- **Department Analytics**: Staff distribution pie chart and salary analysis
- **Revenue Breakdown**: Interactive charts by product category
- **Real-time Data**: Live updates from PostgreSQL database

### 👥 Users Management
- **Interactive Table**: View all users with inline editing capabilities
- **Bulk Updates**: Edit multiple users and save changes in batch
- **Add New Users**: Form-based user creation with validation
- **Department Management**: Dropdown selection for departments
- **Salary Formatting**: Currency display with proper validation

### 🛒 Orders Management
- **Orders Table**: View all orders with status and details
- **Create Orders**: Link orders to existing users via dropdown
- **Order Tracking**: Status management (pending, completed, shipped, cancelled)
- **Product Categories**: Electronics, Books, Clothing, Home, Sports

### 📈 Analytics Dashboard
- **Page Views**: Time-series charts showing traffic trends
- **Bounce Rate Analysis**: User engagement metrics over time
- **Performance Summary**: Top-performing pages and statistics
- **Interactive Visualizations**: Plotly charts with theme adaptation

## 🔧 Configuration

### Database Configuration
Update database settings in `main.py`:

```python
DATABASE_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "database": "streamlit_demo",
    "user": "streamlit_user",
    "password": "streamlit123"
}
```

### API Configuration
Update API base URL in `streamlit_app.py`:

```python
API_BASE_URL = "http://localhost:8000"
```

## 🎨 Theming

The application features an intelligent theming system that:

- **Automatically detects** browser/system dark mode preference
- **Dynamically switches** between light and dark themes
- **Adapts all components**: Streamlit widgets, Plotly charts, custom styling
- **CSS Variables**: Uses modern CSS custom properties for consistent theming
- **Real-time Updates**: Changes instantly when system theme is modified

### Theme Colors

```css
/* Light Mode */
--primary-bg: #ffffff
--secondary-bg: #f0f2f6
--text-color: #262730
--accent-color: #F39C12

/* Dark Mode */
--primary-bg: #14131f
--secondary-bg: #1e1d2e
--text-color: #ffffff
--accent-color: #F39C12
```

## 🚀 API Endpoints

### Users
- `GET /users` - Get all users with pagination
- `GET /users/{user_id}` - Get specific user
- `POST /users` - Create new user
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Soft delete user

### Orders
- `GET /orders` - Get all orders with pagination
- `GET /orders/user/{user_id}` - Get user-specific orders
- `POST /orders` - Create new order

### Analytics
- `GET /analytics/page-views` - Get page view analytics
- `POST /analytics/page-views` - Add page view record

### Dashboard
- `GET /dashboard/summary` - Get dashboard statistics
- `GET /dashboard/revenue-by-category` - Revenue breakdown

## 🧪 Testing

### Manual Testing
```bash
# Test API health
curl http://localhost:8000/health

# Get users
curl http://localhost:8000/users

# Create user
curl -X POST "http://localhost:8000/users" \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "email": "test@example.com", "full_name": "Test User", "department": "Engineering", "salary": 75000}'
```

### Interactive Testing
- Visit http://localhost:8000/docs for Swagger UI
- Use the Streamlit interface for end-to-end testing

## 🛠️ Development

### Adding New Features

1. **Database Changes**: Update SQL schema and migration scripts
2. **API Endpoints**: Add new routes in `main.py` with proper validation
3. **Frontend Pages**: Create new pages in `streamlit_app.py`
4. **Styling**: Update CSS variables for consistent theming

### Code Style
- **FastAPI**: Follow REST conventions and use Pydantic models
- **Streamlit**: Use session state for complex interactions
- **Database**: Use parameterized queries and proper error handling

## 🔍 Troubleshooting

### Common Issues

**API Connection Failed (500 Error)**
- Check PostgreSQL container is running: `docker ps`
- Verify database credentials in `main.py`
- Check FastAPI terminal for detailed error messages

**Database Connection Issues**
```bash
# Test manual connection
docker exec -it postgres_postgres_1 psql -U streamlit_user -d streamlit_demo

# Reset user password if needed
docker exec -it postgres_postgres_1 psql -U postgres -c "ALTER USER streamlit_user WITH PASSWORD 'streamlit123';"
```

**Dependency Issues**
```bash
# Clear UV cache and reinstall
rm -rf .venv uv.lock
uv sync
```

**Port Conflicts**
- FastAPI: Change port with `--port 8001`
- Streamlit: Use `--server.port 8502`
- PostgreSQL: Modify Docker port mapping `-p 5433:5432`

## 📊 Sample Data

The application comes with pre-populated sample data:
- **10 Users** across different departments (Engineering, Marketing, Sales, HR, Finance, Operations)
- **15 Orders** with various statuses and product categories
- **Analytics Data** with page views and performance metrics

## 🚢 Deployment

### Production Considerations
- Use environment variables for database credentials
- Add authentication and authorization
- Implement connection pooling
- Add logging and monitoring
- Use HTTPS in production
- Consider Docker Compose for orchestration

### Docker Deployment
```bash
# Build application image
docker build -t fastapi-streamlit-app .

# Run with Docker Compose
docker-compose up -d
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **FastAPI** - Modern, fast web framework for building APIs
- **Streamlit** - The fastest way to build and share data apps
- **PostgreSQL** - The world's most advanced open source database
- **UV** - An extremely fast Python package installer and resolver
- **Plotly** - Interactive graphing library for Python

## 📞 Support

If you have any questions or run into issues:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the [API Documentation](http://localhost:8000/docs) when running
3. Open an issue in the repository
4. Check existing issues for similar problems

---

**Built with ❤️ using FastAPI, PostgreSQL, Streamlit, and UV**
