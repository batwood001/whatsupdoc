class Config():
  def __init__(self):
    self.c = None

  def set(self, config):
    self.c = config

  def get(self):
    return self.c

config = Config()