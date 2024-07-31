from transformers import pipeline, LLaMAForCausalLM, LLaMATokenizer



model = "hf/llama"
tokenizer = LLaMATokenizer.from_pretrained(model)
model_tune = LLaMAForCausalLM.from_pretrained(model)

class Evaluator:

    def __init__(self, args):
        self.args = args

generator = pipeline('text-generation', model=model, tokenizer=tokenizer)


prompt = "Execute and Check a Test prompt. "

response = generator(prompt, max_length=50, num_return_sequences=1)

print(response)



#Try various prompts and check the reponse of model and performance on different prompt