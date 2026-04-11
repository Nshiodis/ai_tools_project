import requests
import json
import logging
from typing import List,Dict,Optional,Callable

logger = logging.getLogger(__name__)

class LLMClient:
    """真实的大模型 API 客户端（使用测试端点，无需 API Key）"""
    def __init__(self,base_url:str="https://httpbin.org/post",
                 timeout:int=10):
        """
        初始化客户端。
        Args:
            base_url: 请求的 URL（默认使用 httpbin 的测试接口）
            timeout: 请求超时时间（秒）
        """
        self.base_url=base_url
        self.timeout=timeout
    def chat(self, messages:List[Dict[str, str]], stream:bool=False,
             callback:Optional[Callable[[str],None]]=None, **kwargs) -> Optional[str]:
        #Callable表示“一个可以被调用的对象”
        """
       发送对话请求（实际是发送到测试服务器，服务器会回显发送的数据）。
       Args:
           messages: 消息列表
           stream: 是否模拟流式输出（因为测试 API 不支持真流式，这里我们手动分块）
           callback: 流式模式下每个块的回调函数
           **kwargs: 其他参数（会被一起发送）
       Returns:
           非流式模式下返回服务器响应的完整文本；流式模式下返回 None
       """
        # kwargs 是 Python 函数定义中的一个特殊语法，用于接收任意多个关键字参数（keyword arguments）
        # 它的作用是把调用时传入的,函数签名中未明确声明的参数，全部打包成一个字典，字典的键是参数名，值是参数值。

        # 构造要发送的数据
        payload = {
            "messages": messages,
            "extra": kwargs
        }

        try:
            logger.info(f"发送请求到 {self.base_url}, 流式模式: {stream}")
            response = requests.post(
                self.base_url,
                json=payload,
                timeout=self.timeout,
                stream=False  # 注意：httpbin 不支持流式响应，所以我们整体获取
            )
            response.raise_for_status() #检查 HTTP 状态码
            data = response.json()  # 服务器返回的 JSON
            # 从返回的数据中提取 "json" 字段，里面就是我们发送的 payload
            reply = json.dumps(data.get("json", {}), ensure_ascii=False, indent=2)
            logger.info("收到响应")

            if not stream:
                return reply
            else:
                # 手动模拟流式输出：将回复分成多个小块，每个小块调用 callback
                # 这里我们按字符分块（也可以按词），并加上一点延迟，让你看到效果
                import time
                chunk_size = 5  # 每 5 个字符作为一个块
                for i in range(0, len(reply), chunk_size):
                    chunk = reply[i:i + chunk_size]
                    if callback:
                        callback(chunk)
                    else:
                        print(chunk, end='', flush=True)
                    time.sleep(0.1)  # 模拟网络延迟
                return None

        except requests.exceptions.Timeout:
            logger.error("请求超时")
            raise   # 重新抛出异常
        except requests.exceptions.ConnectionError:
            logger.error("网络连接错误")
            raise
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP 错误: {e}")
            raise
        except Exception as e:
            logger.error(f"未知错误: {e}")
            raise