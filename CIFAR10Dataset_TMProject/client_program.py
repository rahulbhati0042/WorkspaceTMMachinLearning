import sys
import requests as req


# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nFolder path:", sys.argv[1])
resp = req.request(method='POST', url="http://localhost:1001/uploadImages", data = sys.argv[1])
print(resp.text)