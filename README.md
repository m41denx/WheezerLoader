## WheezerLoader

Basically a DeezLoader fork, but with proxy support.

DeeLogin behaves differently now, you need to create API_GW first
```python
from wheezeloader.deezloader.deegw_api import API_GW
from wheezeloader.deezloader import DeeLogin

gw = API_GW(
            arl = "ARL",
            email = "wheezer@email.com",
            password = "DeezNuts",
            proxies = {
                "http":"socks5://ip:port",
                "https":"socks5://ip:port"
            }
    )

loader = DeeLogin(gw)


# For unknown reasons different parts of code use raw API_GW class
# effectively resetting all our settings. And all that private
# attributes make patching almost impossible.
```

## Installing
`pip install git+https://github.com/cradio/WheezerLoader`