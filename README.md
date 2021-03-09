This is home assignment of Stella Zhou for Sojern  
I finished "compare versions" and "math api" with Python.   
To make the web application code more robust and maintable, I use python exception handler and logger.    

To run the Python Flask Application for "math api"  
`python app.py`   
  
Please use POST request to test APIs and include `"nums" `and `"quant" `as key in body, for example: 

`curl -X POST http://localhost:8010/min -H "Content-type: application/json" -d '{"nums":[1, 2, 3], "quant":3}'`  
   
`curl -X POST http://localhost:8010/max -H "Content-type: application/json" -d '{"nums":[1, 2, 3], "quant":3}'` 
  
`curl -X POST http://localhost:8010/avg -H "Content-type: application/json" -d '{"nums":[1, 2, 3]}'` 

`curl -X POST http://localhost:8010/median -H "Content-type: application/json" -d '{"nums":[1, 2, 3]}'`  
  
`curl -X POST http://localhost:8010/percentile -H "Content-type: application/json" -d '{"nums":[1, 2, 3], "quant":50}'`