import wolframalpha

input = raw_input("Q: ")
app_id = "G7YP7X-6RGXAVV8TX"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print answer
