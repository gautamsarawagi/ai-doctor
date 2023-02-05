from fastapi import APIRouter, Query

from dotenv import load_dotenv
import uvicorn

import os
from langchain.llms import OpenAI

medbot_api_router = APIRouter()

os.environ['OPENAI_API_KEY'] = "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"
llm = OpenAI(temperature=0)
prefix="answer considering yourself as a doctor and if it is not relevant to doctor background say that it is not a relevant question for a doctor"
suffix="Summarise your answer"
@medbot_api_router.get("/bot")
def medbot(text:str):
    
    return {'medboat':llm(prefix+text+suffix)}
