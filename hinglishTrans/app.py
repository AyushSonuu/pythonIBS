from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM

config = PeftConfig.from_pretrained("DrishtiSharma/llama-2-13b-fp16-english-to-hinglish-translation")
model = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-13B-fp16")
model = PeftModel.from_pretrained(model, "DrishtiSharma/llama-2-13b-fp16-english-to-hinglish-translation")

