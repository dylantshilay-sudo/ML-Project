from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database import SessionLocal
from services.webhook_service import handle_webhook
from fastapi import Request, HTTPException
import json

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/webhook/payment")
async def provider_webhook(request: Request, db: Session = Depends(get_db)):
    # 1. On récupère le texte brut d'abord
    body = await request.body()
    
    # 2. On vérifie si c'est vide
    if not body:
        print("[WEBHOOK] Received empty body, ignoring.")
        return {"message": "Empty body"}

    # 3. On essaie de parser le JSON
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        print(f"[WEBHOOK] Invalid JSON received: {body.decode()}")
        raise HTTPException(status_code=400, detail="Invalid JSON format")

    print(f"[WEBHOOK RECEIVED] {data}")

    # 4. On traite les données
    handle_webhook(data, db)

    return {"message": "Webhook received"}
