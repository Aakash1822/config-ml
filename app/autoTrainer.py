from transformer import LLaMAForCausalLM, LLaMATokenizer, Trainer, TrainingArguments
from testflow.dataConverter import DataConverter


model = "hf/llama"
tokenizer = LLaMATokenizer.from_pretrained(model)
model_tune = LLaMAForCausalLM.from_pretrained(model)

class AutoTrainer:

    def __init__(self, args):
            self.args = args
            self.dataConverter = DataConverter()


def tokenize_f(ex):
    return tokenizer(ex['text'], truncation=True, padding='max_length')
     

def train_ev(self):

    tokenized_data = self.dataConverter.transform.map(self.tokenize_f, batched=True)
    #tokenized_data = dataset.map(tokenize_f, batched=True) #sample loader

    training_args = TrainingArguments(
        output_dir = "./results",
        eval_strategy = "epoch",
        learning_rate = 2e-5,
        per_device_train_batch_size = 2,
        per_device_eval_batch_size = 2,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_step=10,
        no_cuda=True


    )

    trainer = Trainer(
        model = model,
        args = training_args,
        train_dataset = tokenized_data
    )

    trainer.train()
    