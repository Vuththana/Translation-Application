from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain_core.prompts import PromptTemplate
from detect_injection import is_prompt_injection
from detct_toxic import is_inappropriate

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")

USER_PROMPT = PromptTemplate.from_template("Input: {input}\n Target:{target}\nTranslation:")

SYSTEM_PROMPT = "You are a strict translation engine. Translate the input text directly into the requested language."

while True:
    text_to_translate = input("Enter text to translate (q to quit): ").strip()
    if text_to_translate.lower() == "q":
        break

    if not text_to_translate:
        continue

    if  is_inappropriate(text_to_translate):
        print("\n[Blocked]: Inappropriate or offensive content cannot be translated.")
        continue

    if  is_prompt_injection(text_to_translate):
        print("\n[Blocked]: You are not allowed to do this!")
        continue

    language_to_translate = input("Enter language to translate (q to quit): ").strip()

    if language_to_translate.lower() == "q":
        break

    if not language_to_translate:
        continue

    if  is_prompt_injection(language_to_translate):
        print("\n[Blocked]: You are not allowed to do this!")
        continue

    instruction = USER_PROMPT.format(input=text_to_translate, target=language_to_translate)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": instruction},
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    outputs = model.generate(**inputs, max_new_tokens=120)
    translated_text = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    print(f"Input: {text_to_translate}")
    print(f"Language: {language_to_translate}")
    print(f"Translated: {translated_text}")

    text_to_translate = None
    language_to_translate = None
