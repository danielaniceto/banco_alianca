import uuid
import json

class Cliente:
  def __init__(self, nome, documento):
    self.id = str(uuid.uuid4())
    self.nome = nome
    self.documento = documento

  def __str__(self):
    return json.dumps(self, default=lambda o: o.__dict__,
      sort_keys=True, indent=4)
