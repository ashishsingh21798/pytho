import wikipedia
import wolframalpha

while True:
    input = raw_input("Q: ")

    try:
        #wolframalpha
        app_id = "G7YP7X-6RGXAVV8TX"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print answer
    except:
        #wikipedia
        print wikipedia.summary(input)
