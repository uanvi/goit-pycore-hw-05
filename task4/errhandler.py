def input_error(args_count):
    """Decorator to validate arguments count
    """
    def decorator(func):
        def wrapper(args, contacts):
            if len(args) != args_count:
                return False, f"Command should have '{args_count}' arguments."
            return func(args, contacts)
        return wrapper
    return decorator