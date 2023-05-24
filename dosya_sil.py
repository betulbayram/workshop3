import os

if os.path.exists("deneme.txt"):
    print("Dosya Bulundu. Siliniyor...")
    os.remove("deneme.txt")
    print("Silindi")
else:
    print("Dosya bulunamadi.")

# Error Handling
# try:
#     os.remove("deneme.txt")
# except:
#     print("Dosya Bulunamadi.")
# finally:
#     print("Hep çalışır")