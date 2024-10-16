def validate_categoric(categoria):
  return categoria.isalpha()

def handle_invalid_categoric(categoria):
  with open("invalid_categoric.txt", "a") as f:
    f.write(f"{categoria}\n")