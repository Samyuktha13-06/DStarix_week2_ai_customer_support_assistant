# pyrefly: ignore [missing-import]
from langchain_core.output_parsers import StrOutputParser

from prompts.support_prompts import support_prompt
from utils.llm import llm

output_parser = StrOutputParser()

support_chain = (
    support_prompt
    | llm
    | output_parser
)