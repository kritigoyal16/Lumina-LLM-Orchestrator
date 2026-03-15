import os
from loguru import logger
from core.engine import LuminaOrchestrator
from pydantic import BaseModel

class AnalysisResult(BaseModel):
    analysis: str
    key_findings: list[str]
    optimization_strategy: str

def main():
    print("--- Lumina-LLM-Orchestrator Demo ---")
    
    # Initialize engine
    # In production, use os.getenv("LLM_API_KEY")
    engine = LuminaOrchestrator(api_key="mock-api-key")

    prompt = \"\"\"
    Task: Provide a detailed analysis of vLLM's memory management.
    Requirements: Return a structured JSON with 'analysis', 'key_findings' (list), and 'optimization_strategy'.
    \"\"\"

    logger.info("Starting orchestrated LLM task...")
    
    try:
        result = engine.execute_with_correction(prompt, AnalysisResult)
        print("\n✅ STRUCTURED AI RESPONSE:")
        print(result.json(indent=2))
    except Exception as e:
        logger.error(f"Demo failed: {str(e)}")

if __name__ == "__main__":
    main()