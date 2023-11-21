
## http 통신

```python
import requests

def httpcliet():
	url = ''
	files = {'file': open('', 'rb')}
	
	response = requests.post(url, files=files) # SSL 인증을 위해 필요한 경우
	print(response.text)

httpcliet()


```
