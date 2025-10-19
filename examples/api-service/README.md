# FastAPI Microservice Setup

**Arsenal configuration for backend API services**

---

## 🎯 What This Is

A focused Arsenal setup for backend API developers who want:
- ✅ Production-ready REST API patterns
- ✅ Database integration best practices
- ✅ Automated testing and security
- ✅ API documentation automation
- ✅ Microservice architecture support

**Perfect for:**
- Backend API services
- Microservices
- GraphQL APIs
- REST APIs
- Internal services

---

## ⚡ Quick Start

### Step 1: Create API Project

```bash
# Install Arsenals
curl -sSL https://raw.githubusercontent.com/ChrisTansey007/arsenal-integration-hub/main/scripts/install-all.sh | bash

# Create API project
mkdir my-api-service && cd my-api-service
```

### Step 2: Setup Arsenal

```bash
# Create structure
mkdir -p .windsurf/{memories,workflows}

# Copy FastAPI Memory
cp ~/arsenals/windsurf-memories-arsenal/project-types/fastapi-memory.md \
   .windsurf/memories/

# Copy workflows
cp ~/arsenals/ai-workflows-arsenal/windsurf/development/*.md \
   .windsurf/workflows/

cp ~/arsenals/ai-workflows-arsenal/windsurf/code-quality/*.md \
   .windsurf/workflows/
```

### Step 3: Initialize FastAPI

```bash
# Open in Windsurf
windsurf .

# Ask Cascade:
"Initialize a FastAPI project with:
- Project structure
- PostgreSQL + SQLAlchemy
- Alembic migrations
- JWT authentication
- API versioning (/api/v1/)
- Docker setup
- pytest configuration"
```

**Result:** Complete API project in minutes! ✨

---

## 📁 API Project Structure

```
my-api-service/
├── .windsurf/
│   ├── memories/
│   │   ├── fastapi-memory.md           # FastAPI context
│   │   ├── api-architecture.md         # API design
│   │   └── database-patterns.md        # DB patterns
│   │
│   └── workflows/
│       ├── run-tests-and-fix.md        # Testing
│       ├── security-scan.md            # Security
│       ├── code-review-assistant.md    # Review
│       └── api-docs-generator.md       # Docs
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── auth.py
│   │       │   ├── users.py
│   │       │   └── items.py
│   │       └── __init__.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── deps.py
│   │
│   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── session.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   └── auth_service.py
│   │
│   └── main.py
│
├── tests/
│   ├── api/
│   ├── services/
│   └── conftest.py
│
├── alembic/
│   └── versions/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 💭 API Architecture Memory

`.windsurf/memories/api-architecture.md`:

```markdown
# API Service Architecture

## API Design Principles

### RESTful Standards
- Use proper HTTP methods (GET, POST, PUT, DELETE)
- Consistent URL structure
- Proper status codes
- HATEOAS when appropriate

### Versioning
- All routes under /api/v1/
- Version in URL, not headers
- Maintain backwards compatibility

### Response Format

**Success:**
\`\`\`json
{
  "data": { /* response data */ },
  "meta": {
    "timestamp": "2025-01-19T12:00:00Z",
    "version": "1.0.0"
  }
}
\`\`\`

**Error:**
\`\`\`json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": [...]
  }
}
\`\`\`

## Database Patterns

### Service Layer
- All business logic in services
- Keep endpoints thin
- Services are reusable

### Repository Pattern
- Abstract database access
- Easy to test
- Swappable implementations

### Migrations
- Always use Alembic
- Never modify database directly
- Up AND down migrations

## Authentication

### JWT Flow
1. POST /api/v1/auth/login → access token
2. Include in headers: Authorization: Bearer {token}
3. Validate on protected endpoints
4. Refresh tokens for long sessions

### Security
- Passwords hashed with bcrypt
- Tokens expire (30 min access, 7 day refresh)
- Rate limiting on auth endpoints
- CORS configured properly

## Testing Strategy

### Unit Tests
- Test services independently
- Mock external dependencies
- Fast execution

### Integration Tests
- Test API endpoints
- Use test database
- Real HTTP requests

### Coverage Requirements
- Services: 90%+
- Endpoints: 80%+
- Models: 70%+
- Overall: 80%+

## Performance

### Caching
- Redis for sessions
- Cache database queries
- ETags for responses

### Database
- Indexes on foreign keys
- Eager loading (avoid N+1)
- Connection pooling
- Query optimization

### Async Operations
- Use async/await everywhere
- Background tasks for slow operations
- Async database sessions
```

---

## 🚀 API Development Workflow

### Building New Endpoint

**Step 1: Ask Cascade**
```
"Create a new endpoint for blog posts with:
- GET /api/v1/posts (list with pagination)
- GET /api/v1/posts/{id} (single post)
- POST /api/v1/posts (create, auth required)
- PUT /api/v1/posts/{id} (update, auth required)
- DELETE /api/v1/posts/{id} (delete, auth required)

Include:
- SQLAlchemy model
- Pydantic schemas
- Service layer
- Tests
- Migration"
```

**Step 2: Cascade Generates**
- Database model (`app/db/models/post.py`)
- Schemas (`app/db/schemas/post.py`)
- Service (`app/services/post_service.py`)
- Endpoints (`app/api/v1/endpoints/posts.py`)
- Tests (`tests/api/test_posts.py`)
- Migration (Alembic)

**Step 3: Review & Test**
```bash
# Run tests
/run-tests-and-fix

# Check security
/security-scan

# Review code
/code-review-assistant
```

**Step 4: Deploy**
```bash
# Create PR
/commit-and-pr

# After merge
docker build -t my-api:latest .
docker push my-api:latest
```

---

## 💡 Example API Conversations

### Example 1: Add Authentication

**You:**
```
"Implement JWT authentication with:
- Login endpoint (email + password)
- Signup endpoint
- Password hashing with bcrypt
- Access and refresh tokens
- Token refresh endpoint
- Middleware for protected routes"
```

**Cascade (with FastAPI Memory):**
- Creates `app/core/security.py` with JWT functions
- Creates `app/api/v1/endpoints/auth.py` with endpoints
- Adds authentication dependency in `app/core/deps.py`
- Creates user service with password hashing
- Adds comprehensive tests
- Updates API documentation

**Result:** Production-ready auth in 10 minutes!

### Example 2: Add Database Model

**You:**
```
"Create a Product model with:
- name, description, price, stock
- category relationship
- created_at, updated_at timestamps
- Soft deletes
- Full CRUD endpoints"
```

**Cascade:**
- SQLAlchemy model with relationships
- Pydantic schemas (Create, Update, Response)
- Service layer with business logic
- CRUD endpoints with validation
- Alembic migration
- Unit and integration tests

**Result:** Complete feature stack!

### Example 3: Add Pagination

**You:**
```
"Add pagination to all list endpoints with:
- page and limit query params
- Total count in response
- Links to next/prev pages
- Consistent across all endpoints"
```

**Cascade:**
- Creates pagination utility
- Updates all list endpoints
- Adds pagination to response schemas
- Updates tests
- Documents in OpenAPI

**Result:** Consistent pagination everywhere!

---

## 🔧 API-Specific Workflows

### Testing Workflow

```bash
# Run all tests
/run-tests-and-fix

# What it does:
1. Runs pytest
2. Shows coverage report
3. Identifies failures
4. Suggests fixes
5. Auto-fixes when possible
```

### Security Workflow

```bash
# Comprehensive security scan
/security-scan

# Checks:
- Dependency vulnerabilities
- SQL injection risks
- XSS vulnerabilities
- Authentication issues
- Authorization gaps
- Secret leaks
```

### API Documentation

```bash
# Generate/update docs
/update-api-docs

# Generates:
- OpenAPI/Swagger spec
- README API reference
- Example requests
- Response schemas
```

---

## 📊 API Best Practices

### Endpoint Design

**Good:**
```python
@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> UserResponse:
    """Get user by ID."""
    user = await user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

**Why:**
- Type hints everywhere
- Dependency injection
- Proper error handling
- Response model validation
- Docstring for API docs

### Service Layer

**Good:**
```python
class UserService:
    @staticmethod
    async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
        """Create a new user."""
        # Check if email exists
        existing = await UserService.get_by_email(db, user_in.email)
        if existing:
            raise ValueError("Email already registered")
        
        # Hash password
        hashed_password = get_password_hash(user_in.password)
        
        # Create user
        user = User(
            email=user_in.email,
            hashed_password=hashed_password,
            full_name=user_in.full_name
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
        
        # Log event
        logger.info(f"User created: {user.email}")
        
        return user
```

**Why:**
- Business logic in service
- Validation and error handling
- Logging for debugging
- Reusable across endpoints

### Error Handling

**Consistent errors:**
```python
class APIException(HTTPException):
    def __init__(self, status_code: int, code: str, message: str):
        super().__init__(
            status_code=status_code,
            detail={"code": code, "message": message}
        )

# Usage
raise APIException(400, "INVALID_INPUT", "Email is required")
```

---

## 🔒 Security Checklist

### Pre-Production

- [ ] All secrets in environment variables
- [ ] SQL injection prevention (using ORM)
- [ ] Input validation on all endpoints
- [ ] Rate limiting configured
- [ ] CORS properly configured
- [ ] HTTPS enforced
- [ ] Authentication on protected routes
- [ ] Authorization checks
- [ ] Sensitive data encrypted
- [ ] Security headers set
- [ ] Dependencies updated
- [ ] Security scan passed

### Use Security Workflow

```bash
/security-scan

# Automated checks for all items above
# Reports critical issues
# Suggests fixes
```

---

## 🚀 Deployment

### Docker Setup

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/dbname
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=dbname
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Deploy Commands

```bash
# Build
docker build -t my-api:latest .

# Run locally
docker-compose up

# Deploy to production
docker push my-api:latest
kubectl apply -f k8s/deployment.yaml
```

---

## 📊 Performance Tips

### Database Optimization

```python
# Bad: N+1 queries
users = await db.execute(select(User))
for user in users:
    posts = await db.execute(select(Post).where(Post.user_id == user.id))

# Good: Eager loading
users = await db.execute(
    select(User).options(selectinload(User.posts))
)
```

### Caching

```python
from redis import asyncio as aioredis

async def get_user_cached(user_id: int):
    # Check cache
    cached = await redis.get(f"user:{user_id}")
    if cached:
        return json.loads(cached)
    
    # Query database
    user = await user_service.get_user(db, user_id)
    
    # Cache result
    await redis.setex(f"user:{user_id}", 3600, json.dumps(user.dict()))
    
    return user
```

---

## 📈 Monitoring

### Logging

```python
import logging

logger = logging.getLogger(__name__)

# Usage
logger.info("User logged in", extra={"user_id": user.id})
logger.error("Database error", exc_info=True)
```

### Metrics

```python
from prometheus_client import Counter, Histogram

request_count = Counter('api_requests_total', 'Total requests')
request_duration = Histogram('api_request_duration_seconds', 'Request duration')

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    request_count.inc()
    with request_duration.time():
        response = await call_next(request)
    return response
```

---

## 🎉 Success Metrics

### Before Arsenal

- ❌ Inconsistent API design
- ❌ Missing tests
- ❌ Security vulnerabilities
- ❌ Poor documentation
- ❌ Slow development

### After Arsenal

- ✅ Consistent REST patterns
- ✅ 80%+ test coverage
- ✅ Security best practices
- ✅ Auto-generated docs
- ✅ 3x faster development

---

**API Arsenal = Production-Ready APIs, Fast!** 🚀
