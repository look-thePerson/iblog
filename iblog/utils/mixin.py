from typing import Any, Callable


class mixin:
    """
        装饰器
        将给定方法混入指定类中，作为该类实例的方法

        @mixin(func)
        class Cls:
            pass
    """

    def __init__(self, *funcs: Callable[[type, Any], Any]) -> None:
        self.method_dict = {func.__name__: func for func in funcs}

    def __call__(self, cls: type) -> type:
        return type('MixinClass', (cls,), self.method_dict)
