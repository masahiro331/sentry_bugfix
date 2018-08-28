import logging
import sentry_sdk

sentry_sdk.init(dsn="YOUR SENTRY_DSN")

def main():
    try:
        raise
    except Exception:
        return sub()

def sub():
    raise

if __name__ == '__main__':
    main()