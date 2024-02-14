from functools import wraps

def override(func):
    """
    Decorator to override a function from an older version of Telethon with the same function from a newer version.

    Args:
        func: The function to override.

    Returns:
        The overridden function.
    """

    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        return result

    return wrapper
