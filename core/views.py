from django.shortcuts import render
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

print("Hukuk AI Motoru Hazırlanıyor...")
client = QdrantClient("localhost", port=6333)
model = SentenceTransformer('BAAI/bge-m3')
COLLECTION_NAME = "hukuk_ai_kararlar"

def index(request):
    results = []
    user_paragraph = ""
    if request.method == "POST":
        user_paragraph = request.POST.get("olay_metni", "")
        if user_paragraph:
            query_vector = model.encode(user_paragraph).tolist()
            response = client.query_points(
                collection_name=COLLECTION_NAME,
                query=query_vector,
                limit=5,
                with_payload=True
            )
            
            for hit in response.points:
                results.append({
                    "score": round(hit.score * 100, 1),
                    "no": hit.payload.get("basvuru_no"),
                    "tarih": hit.payload.get("karar_tarihi"),
                    "metin": hit.payload.get("text"),
                    "ozet": hit.payload.get("text")[:500] + "..."
                })

    return render(request, "core/index.html", {
        "results": results, 
        "user_paragraph": user_paragraph
    })
