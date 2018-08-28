import logging
import sentry_sdk

sentry_sdk.init(dsn="https://fcf7ba8a60654acdbf6a5e7a69703dab@sentry.io/1270125")

def main():
    try:
        raise
    except Exception:
        return sub()

def sub():
    raise

if __name__ == '__main__':
    main()