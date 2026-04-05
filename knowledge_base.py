import os

def load_knowledge_base(folder="knowledge_base"):
    combined_text = ""
    # This loop looks into your folder and reads every .txt file
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename), "r") as f:
                combined_text += f"\n\n--- {filename} ---\n"
                combined_text += f.read()
    return combined_text