from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('qualifire/prompt-injection-sentinel')
model = AutoModelForSequenceClassification.from_pretrained('qualifire/prompt-injection-sentinel')

pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)

def is_prompt_injection(text: str) -> bool:
    result = pipe(text)
    for res in result:
        if res["label"].lower() == "jailbreak":
            return True
    return False