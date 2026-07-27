from mcp.server.fastmcp import FastMCP
import sqlite3

mcp = FastMCP("candidate-db")
DB_PATH = "candidates.db"

@mcp.tool()
def get_candidate(candidate_id: int) -> dict:
    """Fetch a single candidate by ID from the database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute("SELECT * FROM candidates WHERE id = ?", (candidate_id,)).fetchone()
    conn.close()
    return dict(row) if row else {"error": "not found"}

@mcp.tool()
def list_candidates() -> list:
    """List all candidates in the database with their skills."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT id, name, skills FROM candidates").fetchall()
    conn.close()
    return [dict(r) for r in rows]

if __name__ == "__main__":
    mcp.run()