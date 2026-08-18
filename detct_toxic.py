from transformers import pipeline

moderation_guard = pipeline(
    "text-classification",
    model="unitary/toxic-bert"
)

def is_inappropriate(text:str, threshold: float = 0.7) -> bool:
    results = moderation_guard(text)
    for res in results:
        if res["label"].lower() in ["toxic", "severe_toxic", "insult", "threat"] and res["score"] >= threshold:
            return True
    return False