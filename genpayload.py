import os
import json

payload = []

for assn in os.listdir("./essays/"):
    if (not os.path.isdir("./essays/%s" % assn)): continue
    essay = None
    prompt = None
    for file in os.listdir("./essays/%s" % assn):
        with open(os.path.join("./essays/%s/%s" % (assn, file)), encoding='utf-8') as f:
            text = "\n".join(f.readlines())
            if (file == "essay.txt"):
                essay = text
            elif (file == "prompt.txt"):
                prompt = text
            else:
                raise Exception("Unexpected File Type")
    if (not essay or not prompt):
        raise Exception("Essay or Prompt not found")

    payload.append({"messages": [
        { "role": "user", "content": prompt },
        { "role": "assistant", "content": essay }
    ]})


with open("payload.jsonl", "w", encoding='utf-8') as f:
    for message in payload:
        f.write(json.dumps(message) + "\n")