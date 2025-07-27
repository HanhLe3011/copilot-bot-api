from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # hoặc giới hạn domain Copilot Studio
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question")
    user = data.get("from")

    # Xử lý demo: sinh câu trả lời
    answer = f"Chào {user}, bạn hỏi: “{question}” → Đây là câu trả lời demo."

    return {"answer": answer}
