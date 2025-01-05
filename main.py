from exa_py import Exa

exa = Exa(api_key="826622aa-6069-447a-8d57-198325e95e99")

query = input('Search here: ')
response = exa.search(
  query,
  num_results=10,
  type='keyword',
  include_domains=['https://www.tiktok.com'],
)
for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()

print(response)