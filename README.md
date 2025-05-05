
# StepTech Assignment

## 📦 Environment Setup

1. **Install Python 3.x**
2. **Install Flask using pip:**

```bash
pip install flask
```

---

## 🗄️ Database Interaction

1️⃣ **Create a MySQL database named `users`:**

```sql
CREATE DATABASE users;
```

2️⃣ **Design a table `users`:**

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(100)
);
```

3️⃣ **Insert sample data into `users` table:**

```sql
INSERT INTO users (id, name, email, role)
VALUES (1, "john", "john@gmail.com", "Manager");
```

4️⃣ **Retrieve all users from `users` table:**

```sql
SELECT * FROM users;
```

5️⃣ **Retrieve a specific user by their ID:**

```sql
SELECT * FROM users WHERE id = 1;
```

---

