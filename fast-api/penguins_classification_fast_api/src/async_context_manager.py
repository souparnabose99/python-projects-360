from fastapi import FastAPI
from contextlib import asynccontextmanager

ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Set up the ML model here

    yield
    # Clean up the models and release resources
    ml_models.clear()

