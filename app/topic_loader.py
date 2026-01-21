import yaml

def load_topics(path="topics.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_topic_cfg(cfg, topic):
    return cfg["topics"][topic]
  
