from typing import Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Notes API - Starter")


class NoteCreate(BaseModel):
    title: str
    content: str


class Note(NoteCreate):
    id: int


# In-memory store
_DB: Dict[int, Note] = {}
_NEXT_ID = 1


@app.get("/notes")
def list_notes():
    return list(_DB.values())


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    note = _DB.get(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.post("/notes", status_code=201)
def create_note(payload: NoteCreate):
    global _NEXT_ID
    note = Note(id=_NEXT_ID, **payload.dict())
    _DB[_NEXT_ID] = note
    _NEXT_ID += 1
    return note


@app.put("/notes/{note_id}")
def update_note(note_id: int, payload: NoteCreate):
    note = _DB.get(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    updated = Note(id=note_id, **payload.dict())
    _DB[note_id] = updated
    return updated


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    if note_id not in _DB:
        raise HTTPException(status_code=404, detail="Note not found")
    del _DB[note_id]


if __name__ == "__main__":
    # Run directly: python starter-code.py
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
