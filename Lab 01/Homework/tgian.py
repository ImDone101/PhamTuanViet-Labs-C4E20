from datetime import datetime
now = str(datetime.now())[11:]
limit = now[:5]
print(limit)
