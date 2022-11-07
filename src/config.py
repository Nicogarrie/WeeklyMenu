import dotenv
import pydantic
import sentry_sdk


class Settings(pydantic.BaseSettings):
    sentry_dsn: str
    environment: str

    class Config:
        env_file = dotenv.find_dotenv()


settings = Settings()

sentry_sdk.init(
    dsn=settings.sentry_dsn,
    environment=settings.environment,
    traces_sample_rate=1.0,
)
