from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


tokenizer = AutoTokenizer.from_pretrained("facebook/llama-2-7b")
model = AutoModelForCausalLM.from_pretrained("facebook/llama-2-7b")


def llama(prompt: str) -> str:
    try:
        # Tokenize input prompt
        inputs = tokenizer(prompt, return_tensors="pt")

        # Generate output
        with torch.no_grad():
            outputs = model.generate(inputs.input_ids, max_length=200)

        # Decode output tokens
        response_str = tokenizer.decode(outputs[0], skip_special_tokens=True)

        assert response_str is not None
    except Exception as e:
        print(f"Unhandled exception: {e}")
        response_str = ""

    return response_str
