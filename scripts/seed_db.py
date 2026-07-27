import sqlite3

conn = sqlite3.connect("candidates.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    skills TEXT,
    experience_years REAL
)
""")

candidates = [
    (1, "Jane Doe", "jane.doe@email.com", "Python, Django, PostgreSQL, AWS", 5),
    (2, "John Smith", "john.smith@email.com", "Java, Spring, Docker, Kubernetes", 7),
    (3, "Amit Kumar", "amit.kumar@email.com", "Python, FastAPI, Docker, AWS", 3),
]

conn.executemany("INSERT OR REPLACE INTO candidates VALUES (?, ?, ?, ?, ?)", candidates)
conn.commit()
conn.close()
print("Database seeded.")