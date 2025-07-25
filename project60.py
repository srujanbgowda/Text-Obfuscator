import base64
def obfuscate_text(text):
  base64_bytes = base64.b64encode(text.encode("utf-8"))
  
  base64_text = base64_bytes.decode("utf-8")

  shiftted = "".join(chr(ord(char)+2) for char in base64_text)

  return shiftted

def deobfuscate_text(obfuscated_text):
  shifted_back = "".join(chr(ord(char) -2 )for char in obfuscated_text) 

  decoded_bytes = base64.b64decode(shifted_back.encode("utf-8"))


if __name__ == "__main__":
  original = input("Enter text to obfuscate:")
  obfuscated = obfuscate_text(original)
  print("Obfuscated:", obfuscated)

  recovered = deobfuscate_text(obfuscated)
  print("Recovered:", recovered)

  


    
                                  
                                  
