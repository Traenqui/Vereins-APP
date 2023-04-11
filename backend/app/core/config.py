from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, validator, MongoDsn

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl

    # Security section 
    JWT_ALGORITHM: str
    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int

    #-------------------------------------------------------------#
    # Database
    #-------------------------------------------------------------#

    MONGO_DB_ROOT_USERNAME: str
    MONGO_DB_ROOT_PASSWORD: str
    MONGO_DB_DATABASE: str
    MONGO_DB_PORT: int
    MONGO_DB_HOST: str
    MONGO_DB_QUERY: str

    MONGO_DB_URL: HttpUrl | None = None

    @validator("MONGO_DB_URL", pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, any]) -> any:
        if isinstance(v, str):
            return v
        return MongoDsn.build(
            scheme="mongodb",
            user=values.get("MONGO_DB_ROOT_USERNAME"),
            password=values.get("MONGO_DB_ROOT_PASSWORD"),
            host=values.get("MONGO_DB_HOST"),
            path=f"/{values.get('MONGO_DB_DATABASE') or ''}",
            query=f"{values.get('MONGO_DB_QUERY') or ''}",
        )

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True

settings = Settings()