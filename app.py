import os

environment = os.getenv("ENVIRONMENT", "unknown")
print(f"Deploying to {environment}")
