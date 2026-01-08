from fastapi import FastAPI

app = FastAPI(title="Racket Domain")

racket_data = [
    {"racket_brand": "Babolat"},
    {"racket_brand": "Dunlop"},
    {"racket_brand": "Head"},
    {"racket_brand": "Prince"},
    {"racket_brand": "Wilson"},
    {"racket_brand": "Yonex"}
]

@app.get("/rackets")
def get_rackets_data():
    return {
        "data": racket_data,
        "owner": "Racket Team"
    }
