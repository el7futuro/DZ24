import os.path
import re
from typing import Dict, Callable, Iterable, Generator, Any, Set, Optional, List, Union

file_name = 'data/1apache_logs.txt'


def check_file(file_name: str) -> bool:
    return os.path.exists(file_name)


def read_file(file_name: str) -> Generator[str]:
    with open(file_name) as f:
        for row in f:
            yield row


def filter_query(act: str, data: Iterable[str]) -> Iterable[str]:
    return filter(lambda v: act in v, data)


def map_query(act: str, data: Iterable[str]) -> Iterable[str]:
    column = int(act)
    return map(lambda v: v.split(' ')[column], data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    return set(data)


def sort_query(act: str, data: Iterable[str]) -> Iterable[str]:
    if act == 'asc':
        srt = False
    srt = True
    return sorted(data, reverse=srt)


def limit_query(act: str, data: Iterable[str]) -> Iterable[str]:
    n = int(act)
    return list(data[:n])


def regex_query(data: Iterable[str]) -> Iterable[str]:
    regex = re.compile(data)
    return filter(lambda v: regex.search(v))



dict_function: Dict[str, Callable[..., Iterable[str]]] = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    'regex': regex_query}


def query_action(cmd: str, value: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        gen: Union[Generator, Iterable[str]] = read_file(file_name)
    else:
        gen = data
    res: Iterable[str] = dict_function[cmd](act=value, data=gen)
    return list(res)
