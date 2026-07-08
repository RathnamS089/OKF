import os
from datetime import datetime
import yaml
vault_dir = os.path.expanduser("~/.vault")
def savetookf(title :str,category:str,tags:list,body_content:str):
    os.makedirs(vault_dir,exist_ok=True)
    frontmatter={
        "type":category,
        "title":title,
        "tags":tags,
        "created_at":datetime.now().isoformat()
    }
    yamlstring=yaml.dump(frontmatter,sort_keys=False)
    metadata=f"---\n{yamlstring}---\n\n#{title}\n\n{body_content}"
    words = title.lower().split()
    filename = "-".join(words) + ".md"
    filepath=os.path.join(vault_dir,filename)
    with open(filepath,"w",encoding="utf-8") as f:
        f.write(metadata)
    print(f"OKF concept file generated at:{filepath}")
if __name__=="__main__":
    test_body = "Today I learned how Google's Open Knowledge Format uses Markdown and YAML."
    savetookf(
        title="Learning OKF Basics",
        category="Concept",
        tags=["markdown", "yaml", "beginners"],
        body_content=test_body
    )
    
