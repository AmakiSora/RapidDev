import uvicorn
from fastapi import FastAPI, Header, Body, Form
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse

"""
    FastAPI使用教程
    文档链接:/docs 或 /redoc   
"""
app = FastAPI()


@app.get('/')
def hello_world():
    """HelloWorld"""
    return "Hello,world!"


@app.post('/post')
def post():
    return '这是post请求示例!'


@app.api_route('/methods', methods=['POST', 'GET', 'PUT'])
def method():
    return '多种请求方式示例!'


@app.get('/param/')
def param(p):
    """/param?p=666"""
    return "获取到的param为:" + p


@app.get('/url/{i}')
def url(i):
    """/url/233"""
    return "获取到url中的参数为:" + i


@app.get('/header')
def header(t=Header(None)):
    """header中t=996"""
    return "获取到Header中的参数为:" + t


@app.get('/body')
def body(data=Body(None)):
    """body中参数为007"""
    return "获取到body中的参数为:" + str(data)


@app.get('/form')
def body(a=Form(None), b=Form(None)):
    """form中参数为a=555,b=777"""
    return "获取到form中的参数为:" + str(a) + str(b)


@app.get('/customReturnData')
def custom_return_data():
    """自定义返回体中的herder和code"""
    return JSONResponse(content="返回内容!",
                        status_code=233,
                        headers={'h': 'haha'})


@app.get('/returnHtml')
def return_html():
    """返回Html页面"""
    ht = '''
    <html>
        <body>
            <h1>页面</h1>
        </body>
    </html>
    '''
    return HTMLResponse(content=ht)


@app.get('/returnFile')
def return_file():
    """返回文件"""
    url = 'D:\cosmos\emm\Dg26wbSVAAEjS5P.jpg'
    return FileResponse(url, filename='heart.jpg')


if __name__ == '__main__':
    uvicorn.run(app)
