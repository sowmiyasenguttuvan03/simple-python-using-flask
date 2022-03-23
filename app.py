from flask import Flask,jsonify,request;
import demo

app=Flask(__name__);

@app.get("/new")
def getexample():
    data=demo.getall();
    json_list=[]
    for item in data:
        content={};
        content={'id':item[0],'name':item[1], 'dept':item[2]};
        json_list.append(content);
    return(jsonify(json_list));

@app.post("/postmethod")
def postfunc():
    data = request.get_json();
    print("--data--")
    demo.Insert(data)
    return("Got Data")

@app.patch("/upd")
def updateFunc():
    data=request.get_json();
    print("--data--");
    demo.upd(data);
    return("Got Updated");


@app.delete("/delete/<id>")
def delfunc(id):
    demo.delete(id);
    return("Deleted");


if __name__=='__main__':
    app.run(debug=True, port=1234)




