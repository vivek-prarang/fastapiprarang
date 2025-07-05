
from app.config.settings import settings #?importing settings for config


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )

# *The⁡⁣⁢⁢ run.py ⁡file serves as the entry point for launching the FastAPI application. It utilizes uvicorn to start the server, using configuration settings imported from app.config.settings. The application is set to run in debug mode based on the settings, and listens on the specified host and port.

#^ ⁡⁢⁣⁢𝗨𝘃𝗶𝗰𝗼𝗿𝗻⁡ is an ASGI (Asynchronous Server Gateway Interface) server for Python web applications. It is designed to run
# *asynchronous applications using the `asyncio` library and is commonly used to serve FastAPI and Starlette applications. Uvicorn is known for its performance, simplicity, and ability to handle a large number of simultaneous connections efficiently.

#!after the it go to the app/main.py