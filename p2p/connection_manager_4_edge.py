import socket
import threading
import pickle
import signal
import codecs
import time
import os
from concurrent.futures import ThreadPoolExecutor
from .core_node_list import CoreNodeList
from .message_manager import (
    MessageManager,
    MSG_CORE_LIST,
    MSG_PING,
    MSG_ADD_AS_EDGE,
    ERR_PROTOCOL_UNMATCH,
    ERR_VERSION_UNMATCH,
    OK_WITH_PAYLOAD,
    OK_WITHOUT_PAYLOAD,
)
# 動作確認用の値。本来は30 分(1800) くらいがいいのでは
PING_INTERVAL = 10

