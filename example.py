import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

sentry_logging = LoggingIntegration(
    level=logging.DEBUG,
    event_level=logging.ERROR
)
sentry_sdk.init(dsn="YOUR SENTRY_DSN", integrations=[sentry_logging])

def main():
    try:
        raise
    except Exception:
        return sub()

def sub():
    raise

if __name__ == '__main__':
    main()