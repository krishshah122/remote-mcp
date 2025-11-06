from fastmcp import FastMCP
import random 
import json
mcp=FastMCP(name="simple")
@mcp.tool()
def add(a:int,b:int)->int:
    return a+b
@mcp.tool()
def randno(min:int=1,max:int=100)->int:
    return random.randint(min,max)

if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
