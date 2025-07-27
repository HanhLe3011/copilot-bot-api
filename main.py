from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
import asyncpg

load_dotenv()  # Load .env file

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")
    user = data.get("from", "")

    # Mapping câu hỏi → SQL (đơn giản)
    if "1304" in question:
        query = '''
    SELECT "ACT_OUTPUT" 
    FROM "supportData"."E_FACTORY_OUTPUT_CHANGED"
    WHERE "LINE_NUMBER" LIKE '1304'
    ORDER BY "TIMESTAMP" DESC
    LIMIT 1
'''
    else:
        return {"answer": "Chưa hiểu câu hỏi."}

    # Kết nối DB dùng biến môi trường
    try:
        conn = await asyncpg.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME"),
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT"))
        )
        result = await conn.fetchval(query)
        await conn.close()
    except Exception as e:
        return {"answer": f"Lỗi kết nối hoặc truy vấn DB: {str(e)}"}

    return {"answer": f"Chào {user}, line 1304 hôm nay chạy được {result} sản phẩm."}
