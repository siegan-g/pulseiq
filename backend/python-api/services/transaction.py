from fastapi import FastAPI, Request, HTTPException
import uvicorn

class TransactionService:
    def __init__(self)->None:
        self.webserver = FastAPI(title="Transaction Service",description="A Service to Handle Transactions")
        self.setup_routes()
        pass

    def verify_token(self,request:Request)->bool:
        """
        verify token in request in valid
        """
        token = request.headers.get("Authorization")
        if token != "12345":
            raise HTTPException(status_code=401, detail="Invalid token",headers={})
        

    def setup_routes(self):
        @self.webserver.get("/transact/health")
        def health():
            return {"status":"I'm Alive!"}
        
    def start_server(self):
        uvicorn.run(self.webserver,host="0.0.0.0",port=3000)
            
