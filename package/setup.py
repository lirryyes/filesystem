from distutils.core import   setup
setup(name="package",
           version="1.0",
           description="发送和接收消息",
           long_description="完整接收和发送消息",
           author="liuchun",
           author_email="13435669948@163.com",
           url="www.itheima.com",
           py_modules=[
            "package.send_message",
            "package.receive_message"
           ]

)