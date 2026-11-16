import requests

if __name__ == "__main__":
    # response: requests.Response = requests.get("http://httpbin.org/get")
    # print(response.status_code)
    # print(response.headers)
    # print(response.json())

    # response: requests.Response = requests.get("https://tsukitech.eu")
    # print(response.status_code)
    # print(response.headers)
    # print(response.json())

    response: requests.Response = requests.post("http://httpbin.org/post",
                                                data={"username": "admin", "password": ""})
    print(response.status_code)
    print(response.headers)
    print(response.json())
