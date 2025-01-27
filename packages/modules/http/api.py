import functools
from typing import Callable, Optional

from helpermodules import log
from modules.common import req


def request_value(url: str) -> Optional[float]:
    if "none" == url:
        return None
    else:
        response = req.get_http_session().get(url, timeout=5)
        response.encoding = 'utf-8'
        log.MainLogger().debug("Antwort auf "+str(url)+" "+str(response.text))
        return float(response.text.replace("\n", ""))


def create_request_function(domain: str, path: str) -> Callable[[], Optional[float]]:
    if path == "none":
        return lambda: 0
    else:
        return functools.partial(request_value, domain + path)
