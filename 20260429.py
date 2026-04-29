import traceback
try:
  x=10/0
except:
  log=traceback.format_exc()
  print(log)
  with open("log.txt","w",encoding="utf-8") as f:
    f.write(log)