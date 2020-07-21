Import wolframalpha
Client = wolframalpha.Client('_')
while True:
     query = str(input('Query: '))
     res = client.query(query)
     output = next(res.results).text
     print(output)
