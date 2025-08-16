from fastapi import FastAPI, Request, HTTPException, Depends
import uvicorn
from models.transaction import Transaction
from .strategies.transaction_strategy_factory import TransactionStrategyFactory 

class TransactionService:
    def __init__(self,factory:TransactionStrategyFactory)->None:
        self.factory = factory
        self.webserver = FastAPI(title="Transaction Service",description="A Service to Handle Transactions")
        self.setup_routes()
        pass

    def verify_token(self,request:Request)->bool:
        """
        verify token in request in valid
        """
        token = request.headers.get("Authorization")
        if token != "testpulseiqtoken":
            raise HTTPException(status_code=401, detail="Invalid token",headers={})
        

    def setup_routes(self):
        @self.webserver.get("/transact/health")
        def health():
            return {"status":"I'm Alive!"}

        @self.webserver.post("/transact")
        async def create(transaction:Transaction,token:str=Depends(self.verify_token)):
            try:
                # request_body = await.request.json()
                strategy = self.factory.create(transaction)
                response = strategy.send()
            except Exception as e:
                pass
        
    def start_server(self):
        uvicorn.run(self.webserver,host="0.0.0.0",port=3000)
            
