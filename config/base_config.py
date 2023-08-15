from pydantic import BaseSettings


class Settings(BaseSettings): 
    WAREHOUSE_HOST: str 
    WAREHOUSE_PORT: int 
    WAREHOUSE_TIMEOUT: int
    WAREHOUSE_PERSON_INDEX: str
    WAREHOUSE_USERNAME: str
    WAREHOUSE_PASSWORD: str

    class Config: 
        env_file = '.env'

settings = Settings()
