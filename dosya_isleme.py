# file = open("example.txt", "r")

# result = file.readlines()

# # for i in result:
# #     print(i)

# for i in range(0, len(result)):
#     print(f"indis: {i}\tdeger: {result[i]}")
# file.close()

file = open("example.txt", "a")

file.write("Kamp B23" + "\n")
file.close()
print("some changes")
