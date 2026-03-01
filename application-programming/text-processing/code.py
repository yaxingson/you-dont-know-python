import csv


models = (
  ('openai', 'gpt-5', 'usa'),
  ('google', 'gemini-3-pro', 'usa'),
  ('alibaba', 'qwen-plus', 'china'),
)

with open('models.csv', 'w') as f:
  writer = csv.writer(f, lineterminator='\n')
  for model in models:
    writer.writerow(model)

with open('models.csv') as f:
  reader = csv.reader(f)
  for provider, model, country in reader:
    print(f'{country}: ({provider}, {model})')


